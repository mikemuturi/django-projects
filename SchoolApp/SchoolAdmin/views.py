from django.shortcuts import render, HttpResponse
from .models import Course
from django.db.models import Count

# Create your views here.
def index(request):
    return render(request, 'index.html')



# def courses(request):
#     all_courses = Course.objects.all()
    
#     context = {
#         'all_courses': all_courses
#     }

#     return render(request, 'course.html', context)


