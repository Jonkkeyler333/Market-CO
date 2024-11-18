from django.db import models

class Product(models.Model):
    seller=models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='products')
    name=models.CharField(max_length=255)
    description=models.TextField()
    fabric_type=models.CharField(max_length=255)  # Tipo de tela
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name+ ' - '+self.seller.username

