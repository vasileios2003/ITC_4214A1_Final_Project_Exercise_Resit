from django.db import models
from django.contrib.auth.models import User
from catalogue.models import Book

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('catalogue.Book', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def subtotal(self):
        return self.book.price * self.quantity