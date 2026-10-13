from django.shortcuts import render, get_object_or_404
from .models import Menu

def menu_dish(request):
    menu_list = Menu.objects.all()
    return render(request, 'menu.html', context={'menu': menu_list})

def dish_detail(request, pk):
    dish = get_object_or_404(Menu, pk=pk)
    return render(request, 'dish_detail.html', context={'dish': dish})

def about_us(request):
    return render(request, 'about.html')
