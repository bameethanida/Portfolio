from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


def home(request):
    return render(request, 'home.html')

def aboutme(request):
    return render(request, 'aboutme.html')

def experiences(request):
    return render(request, 'experiences.html')

def projects(request):
    return render(request, 'projects.html')

def activities(request):
    return render(request, 'activities.html')

def contact(request):
    if request.method == 'POST':
        print(request)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})