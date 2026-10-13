from django.db import models


class Menu(models.Model):
    dish_name = models.CharField(max_length=100, null=True)
    caption = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.dish_name
