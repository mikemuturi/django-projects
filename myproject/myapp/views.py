from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserInformationForm
from .models import userInformation
import csv
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UserInformationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserInformationForm()
    return render(request, 'home.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def admin_page(request):
    users = userInformation.objects.all()
    return render(request, 'admin_page.html', {'users': users})

def update_is_active(request, user_id):
    user = userInformation.objects.get(id=user_id)
    user.isActive = not user.isActive
    user.save()
    return redirect('admin_page')

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    users = userInformation.objects.all()
    writer.writerow(['First Name', 'Email', 'Gender', 'IsActive', 'Age'])
    for user in users:
        writer.writerow([user.first_name, user.email, user.gender, user.isActive, user.age])
    
    return response
