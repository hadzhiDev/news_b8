from django.shortcuts import render, redirect

from news.models import News, Category, Comment
from news.forms import NewsForm


def main(request):
    news_list = News.objects.all()
    return render(request, 'index.html', {'news_list': news_list})



def create_news(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.auth = request.user
            news.save()
            return redirect('/')
    return render(request, 'create.html', {'form': form})
