from django.db import models
from multiselectfield import MultiSelectField


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField()
    category_options = [
        ('smartphones', 'Smartphones'),
        ('laptops', 'Laptops'),
        ('tablets', 'Tablets'),
        ('televisions', 'Televisions'),
        ('headphones', 'Headphones'),
        ('cameras', 'Cameras'),
        ('gaming', 'Gaming'),
        ('smart_home', 'Smart Home'),
        ('wearables', 'Wearables'),
        ('accessories', 'Accessories'),
        ('sports', 'Sports'),
        ('bikes', 'Bikes'),
        ('motorcycles', 'Motorcycles'),
        ('other', 'Other'),

    ]
    category = MultiSelectField(max_length=100, choices=category_options)
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.name
