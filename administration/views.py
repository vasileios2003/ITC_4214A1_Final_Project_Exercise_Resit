from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from catalogue.models import Book, Category
from django.contrib.auth.models import User

@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    stats = {
        'book_count': Book.objects.count(),
        'category_count': Category.objects.count(),
        'user_count': User.objects.count(),
    }
    return render(request, 'administration/dashboard.html', stats)