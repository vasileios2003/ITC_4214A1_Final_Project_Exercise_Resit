from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Book, Category, Rating
from django.db.models import Q

def category_items(request, category_name):
    category = get_object_or_404(Category, name__iexact=category_name)
    books = Book.objects.filter(category=category)
    return render(request, 'catalogue/category_items.html', {
        'category': category,
        'books': books
    })

def search_items(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Book.objects.filter(
            Q(name__icontains=query) | Q(author__icontains=query)
        )

    return render(request, 'catalogue/search_results.html', {
        'query': query,
        'results': results
    })

@login_required
def rate_book(request, book_id):
    if request.method == 'POST':
        score = int(request.POST.get('score'))
        book = get_object_or_404(Book, id=book_id)
        rating, _ = Rating.objects.update_or_create(
            user=request.user, book=book, defaults={'score': score}
        )
        return JsonResponse({'success': True, 'new_score': rating.score})
    return JsonResponse({'success': False}, status=400)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    recommendations = Book.objects.filter(category=book.category).exclude(id=book.id)[:4]
    return render(request, 'catalogue/book_detail.html', {
        'book': book,
        'recommendations': recommendations  # fix the typo here
})