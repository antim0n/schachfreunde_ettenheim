from django.shortcuts import render
from .models import Artikel

def home(request):
    articles = Artikel.objects.all()
    lst = []
    for i in range(0, len(articles), 3):
        if i < 10:
            lst.append(articles[i:i + 3])
    return render(request, 'home.html', {'articles': articles, 'articles_chunked' : lst})

def aktuelles(request):
    articles = Artikel.objects.all()
    return render(request, 'aktuelles.html', {'articles': articles})

def der_verein(request):
    return render(request, 'der_verein.html')

def sponsorenbrett(request):
    return render(request, 'sponsorenbrett.html')

def kleidung(request):
    return render(request, 'kleidung.html')

def impressum(request):
    return render(request, 'impressum.html')