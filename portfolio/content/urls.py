from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('skills/', views.skills, name="skills"),
    path('certifications/', views.certifications, name="certifications"),
    path('education/', views.education, name="education"),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('project-entry/', views.project_entry, name="projects-entry")
]
