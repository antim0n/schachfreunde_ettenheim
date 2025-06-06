from django.shortcuts import redirect, render
from .models import Artikel
from .models import Termin
from .forms import ArtikelForm
from .forms import TerminForm

def home(request):
    articles = Artikel.objects.all()
    lst = []
    for i in range(0, len(articles), 3):
        if i < 10:
            lst.append(articles[i:i + 3])
    return render(request, 'home.html', {'articles': articles, 'articles_chunked' : lst})

def aktuelles(request):
    if request.POST:
        form = ArtikelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(aktuelles)

    articles = Artikel.objects.all()
    return render(request, 'aktuelles.html', {'articles': articles, 'form': ArtikelForm })

def der_verein(request):
    return render(request, 'der_verein.html')

def termine(request):
    if request.POST:
        form = TerminForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(termine)
    
    appointments = Termin.objects.all()
    return render(request, 'termine.html', {'appointments': appointments, 'form': TerminForm})

def sponsorenbrett(request):
    return render(request, 'sponsorenbrett.html')

def kleidung(request):
    return render(request, 'kleidung.html')

def kontakt(request):
    return render(request, 'kontakt.html')

def impressum(request):
    return render(request, 'impressum.html')