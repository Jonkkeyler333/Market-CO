from django.db import models

class Order(models.Model):
    client=models.ForeignKey('users.CustomUser',on_delete=models.CASCADE, related_name='orders')
    created_at=models.DateTimeField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} - {self.client.username}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey('products.Product',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

