from django.shortcuts import render, get_object_or_404
from .models import Home, About, Tag, Project, ProjectImage, Experience, Skill, Contact


def home(request):
    homes = Home.objects.first()
    abouts = About.objects.first()
    projects = Project.objects.all()
    tags = Tag.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    contacts = Contact.objects.first()
    return render(
        request,
        "home.html",
        {
            "homes": homes,
            "abouts": abouts,
            "projects": projects,
            "tags": tags,
            "experiences": experiences,
            "skills": skills,
            "contacts": contacts,
        },
    )


# def contact(request):
#     return render(request, "contact.html")


def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})
