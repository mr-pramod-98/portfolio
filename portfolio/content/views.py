from django.shortcuts import render
from .models import Certifications


# Create your views here.
def home(request):
    return render(request, 'home.html')


def skills(request):
    return render(request, 'skills.html')


def certifications(request):
    certificates = Certifications.objects.all()
    return render(request, 'certifications.html', {'certificates': certificates})


def education(request):
    return render(request, 'education.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def project_entry(request):
    return render(request, 'project-entry.html')
