from django.urls import path
from .views import menu_dish, dish_detail, about_us

urlpatterns = [
    path("", menu_dish, name='menu'),
    path("dish/<int:pk>/", dish_detail, name='dish_detail'),
    path("about/", about_us, name='about'),
]
