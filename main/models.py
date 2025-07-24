from django.db import models


# Home Section
class Home(models.Model):
    image = models.ImageField(upload_to="home_images/")

    def __str__(self):
        return "Home Section"


# About Section
class About(models.Model):
    description = models.TextField()
    recent_skills = models.TextField(
        help_text="Enter recent skills separated by commas (e.g., LLMs, Ollama, LangChain)",
        blank=True,
        null=True,
    )

    def __str__(self):
        return "About Section"

    def get_recent_skills(self):
        return [
            skill.strip() for skill in self.recent_skills.split(",") if skill.strip()
        ]


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
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

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
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)

    class Meta:
        ordering = ["-current", "-endDate", "-startDate"]

    def __str__(self):
        return self.organization

    def get_bullet_points(self):
        return [
            point.strip() + "."
            for point in self.description.split(".")
            if point.strip()
        ]


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
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)

    def __str__(self):
        return self.name
