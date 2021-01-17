from django.shortcuts import render


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
    return render(request, 'contact.html')

