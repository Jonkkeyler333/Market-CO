from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    buyer = models.ForeignKey(User, related_name='orders_made', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='orders_received', on_delete=models.CASCADE)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.buyer} a {self.seller}"
