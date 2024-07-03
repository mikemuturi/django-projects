from django.contrib import admin
from .models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['courseName', 'coursePrice', 'courseDuration']

# Register your models here.
admin.site.register(Course, CourseAdmin)

