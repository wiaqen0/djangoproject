from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == "POST":
        try:
            first = request.POST['first']
            last = request.POST['last']
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    return render(request, 'register.html', {'error': 'Username already exists!'})
                elif User.objects.filter(email = email).exists():
                    return render(request, 'register.html', {'error': 'Email already exists!'})
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first, last_name=last)
                    user.save()
                    user = auth.authenticate(username=username, password=password1)
                    auth.login(request, user)
                    messages.info(request, 'Your account has been created successfully!')
                    return redirect('/')
            else:
                return render(request, 'register.html', {'error': 'Password does not match!'})
        except:
            return render(request, 'register.html', {'error': 'Please fill all the fields!'})
    return render(request, 'register.html')