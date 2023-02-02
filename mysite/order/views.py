from django.shortcuts import render, redirect
from calc.models import food, order
from django.contrib.auth.models import User
from django.contrib import messages
import datetime
def delete_order(request, id):
    if request.user.is_authenticated:
        if request.user.username == order.objects.get(id=id).username:
            order.objects.get(id=id).delete()
            return redirect('/order/order')
        else:
            return redirect('/order/order')
    else:
        return redirect("/register/login")
def dynamic_lookup_view(request, id):
    obj = food.objects.get(id = id)
    context = {
        "object": obj
}
    try:
        if request.method == "POST":
            if request.user.is_authenticated:
                username1 = User.objects.get(username=request.user)
            else:
                username1 = request.POST['name']
            address = request.POST['address']
            phone = request.POST['phone']
            foods = obj.name
            quantity = request.POST['quantity']
            now = datetime.datetime.now()
            total_price = obj.price * int(quantity)
            orders = order(username = username1, address=address, phone=phone, food=foods, quantity=quantity, time = now, total_price=total_price)
            orders.save()
            messages.success(request, 'Your order has been created successfully!')
            return redirect('/order/{}'.format(obj.type))
        else:
            return render(request, "order.html", context)
    except:
        context["error"] = "Wrong data filled!"
        return render(request, "order.html", context)
def get_user_order(request):
    if request.user.is_authenticated:
        username1 = User.objects.get(username = request.user)
        orders = order.objects.filter(username = username1)
        context = {
            "name": username1,
            "orders": orders
        }
        return render(request, "check_order.html", context)
    else:
        return redirect('/register/login')
def chicken_order(request):
    orders = food.objects.filter(type='chicken', active=True)
    context = {"orders": orders}
    return render(request, "order_list.html", context)
def combo_order(request):
    orders = food.objects.filter(type='combo', active=True)
    context = {
        "orders": orders}
    return render(request, "order_list.html", context)
def pizza_order(request):
    orders = food.objects.filter(type='pizza', active=True)
    context = {
        "orders": orders}
    return render(request, "order_list.html", context)
def asian_order(request):
    orders = food.objects.filter(type='asian', active=True)
    context = {
        "orders": orders}
    return render(request, "order_list.html", context)
def beverage_order(request):
    orders = food.objects.filter(type='beverage', active=True)
    context = {
        "orders": orders}
    return render(request, "order_list.html", context)