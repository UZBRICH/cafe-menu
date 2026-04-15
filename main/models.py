from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default="🍽️")  # emoji support

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Feedback(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    rating = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)