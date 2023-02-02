from django.contrib import admin
from .models import food, order
# Register your models here.
class Filter_food(admin.ModelAdmin):
    list_display = ('name', 'desc', 'image', 'price', 'type', 'd_price', 'active')
    list_filter = ('type', 'active')
class Filter_order(admin.ModelAdmin):
    list_display = ('username', 'address', 'phone', 'food', 'quantity', 'time')
    list_filter = ('username', 'food')
admin.site.register(food, Filter_food)
admin.site.register(order, Filter_order)