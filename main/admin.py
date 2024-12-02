from django.contrib import admin
from .models import Home, About, Tag, Project, ProjectImage, Experience, Skill, Contact


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tags",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("organization",)


admin.site.register(Home)
admin.site.register(About)
admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill)
admin.site.register(Contact)
