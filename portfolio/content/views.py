from django.shortcuts import render
from .models import Certifications, PersonalProjects, GroupProjects


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
    personal_projects = PersonalProjects.objects.values_list('title')
    group_projects = GroupProjects.objects.values_list('title')
    for i in group_projects:
        print(i)
    return render(request, 'projects.html', {'personal_projects': personal_projects, 'group_projects': group_projects})


def project_details(request, category, title):
    if category == "group-projects":
        details = GroupProjects.objects.get(pk=title)
        is_group_project = True
    else:
        details = PersonalProjects.objects.get(pk=title)
        is_group_project = False

    return render(request, 'project-details.html', {'details': details, 'is_group_project': is_group_project})
