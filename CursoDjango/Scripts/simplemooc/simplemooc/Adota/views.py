from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Animal


def index(request):
    animal = Animal.objects.all()
    template_name = 'Adota/index.html'
    context = {
        'animal': animal
    }
    return render(request, template_name, context)

def cao(request):
    cao = Animal.objects.filter(tipo__equal = Cachorro)
    template_name = 'Adota/cao.html'
    context = {
        'cao':cao
    }
    return render(request, template_name, context)

def gato(request):
    gato = Animal.objects.filter(tipo__icontains = 2)
    template_name = 'Adota/gato.html'
    context = {
        'gato':gato
    }
    return render(request, template_name, context)




def details(request, slug):
    animal = get_object_or_404(Animal, slug=slug)
    context = {}

    context['Animal'] = animal
    template_name = 'Adota/details.html'
    return render(request, template_name, context)