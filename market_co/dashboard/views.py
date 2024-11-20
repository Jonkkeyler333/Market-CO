from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Order
from .forms import ArticleForm

@login_required
def comprador_dashboard(request):
    articles = Article.objects.filter(user=request.user)
    orders = Order.objects.filter(seller=request.user)
    return render(request, 'comprador.html', {'articles': articles, 'orders': orders})

@login_required
def upload_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('comprador_dashboard')
    else:
        form = ArticleForm()
    return render(request, 'upload_article.html', {'form': form})
