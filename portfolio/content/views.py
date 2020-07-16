from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def skills(request):
    return render(request, 'skills.html')


def certifications(request):
    return render(request, 'certifications.html')


def education(request):
    return render(request, 'education.html')


def about(request):
    return render(request, 'about.html')
