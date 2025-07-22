from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalogue.models import Book
from .models import CartItem

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    if not created:
        item.quantity += 1
    item.save()
    return redirect('cart_view')

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in items)
    return render(request, 'cart/cart.html', {'items': items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart_view')