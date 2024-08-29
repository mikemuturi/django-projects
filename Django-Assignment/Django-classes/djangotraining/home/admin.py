from django.contrib import admin # type: ignore
from . models import Course, Subjects

#PASS THIS CLASS TO ADMIN REGISTERED SITE BELOW TO MAKE IT WORK
class CourseAdmin(admin.ModelAdmin): #THIS CLASS LIST OF COURSES IN LIST VIEW AND ENABLE FIELD TO BE EDITED
    list_display = ['courseName', 'coursePrice', 'courseDuration'] #THIS LIST ALL FIELDS
    list_editable = ['coursePrice'] #YOU CAN ADD ALL FIELD YOU WANT TO EDIT HERE

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Subjects)