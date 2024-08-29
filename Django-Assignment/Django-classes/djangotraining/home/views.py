from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .models import Course, Subjects
from django.db.models import Count
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
@login_required(login_url='login')
def courses(request):
    all_courses = Course.objects.all()
    all_subjects = Subjects.objects.annotate(course_count=Count('course'))
    
    context = {
        'allsubjects': all_subjects,
        'allcourses': all_courses
    }

    return render(request, 'course.html', context)

def teachers(request):
    return render(request, 'teacher.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_instance = request.POST['message']

        message = f'Name: {name}\nEmail:{email}\n{message_instance}'

        try:
            send_mail(
                subject,
                message,
                email,  # Sender email
                ['email'], # Receiver email
                fail_silently=False,
            )
            messages.success(request, "Successfully sent")
            return render(request, 'contact.html')
        except Exception as e:
            messages.error(request, f'Error occurred: {e}')    

    return render(request, 'contact.html')

def get_subjects(request):
    all_subjects_list = list(Subjects.objects.all().values())
    return JsonResponse({'subjects': all_subjects_list})

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
                if request.GET.get('next', None):
                    return HttpResponseRedirect(request.GET['next'])
                return redirect('/')
            messages.warning(request, 'Invalid login details')
            return render(request, 'login.html')
        return render(request, 'login.html')
    return redirect('/')
    
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name'] #first_name = request.POST.get('first_name')
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username is already taken!')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'email is taken')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, 
                                                first_name = first_name,
                                                email=email,
                                                password=password) 
                messages.info(request, 'User created!')
                return redirect('login')
        messages.warning(request, 'Password mismatch!')
        return render(request, 'register.html')    
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
