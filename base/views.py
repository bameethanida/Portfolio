from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError
from django.contrib import messages
from .forms import ContactForm


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
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})