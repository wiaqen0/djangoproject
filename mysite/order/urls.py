from django.urls import path
from .views import dynamic_lookup_view, get_user_order, chicken_order, combo_order, asian_order, beverage_order, pizza_order, delete_order
urlpatterns = [
    path('<int:id>', dynamic_lookup_view, name='<int:id>'),
    path('order', get_user_order, name='order'),
    path('chicken', chicken_order, name='chicken_order'),
    path('combo', combo_order, name='combo_order'),
    path('pizza', pizza_order, name='pizza_order'),
    path('asian', asian_order, name='asian_order'),
    path('beverage', beverage_order, name='beverage_order'),
    path('delete/<int:id>', delete_order, name='delete_order'),
]