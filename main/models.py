from django.db import models


# Home Section
class Home(models.Model):
    image = models.ImageField(upload_to="home_images/")

    def __str__(self):
        return "Home Section"


# About Section
class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return "About Section"


# Project Section
# Project Tags - Python, pandas, OpenCV etc ...
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Project Name
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)
    # organization = models.CharField(max_length=200, blank=True)
    # start_data = models.DateField(blank=True, null=True)
    # end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


# Project Images
class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"


# Experience Section
class Experience(models.Model):
    organization = models.CharField(max_length=200)
    jobTitle = models.CharField(max_length=200)
    description = models.TextField()
    startData = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.organization


# Skills
class Skill(models.Model):
    skillName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skillName


# Contact Information
class Contact(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    phone = models.CharField(max_length=12)
    profilePicture = models.ImageField(upload_to="profile_images/")
    email = models.EmailField()
    github = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name
