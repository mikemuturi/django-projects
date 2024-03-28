# # from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# from django.core.exceptions import ObjectDoesNotExist



# def register(request):
#     if request.method == 'POST':
#          form = UserRegisterForm(request.POST)
#          if form.is_valid():
#               form.save()
#               username = form.cleaned_data.get('username')
#               messages.success(request, f'Your account has been created! login')
#               return redirect('login')  # Redirect to the home page
#     else:
#          form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})

# @login_required
# def profile(request):
#    if request.method == 'POST':
#      u_form = UserUpdateForm(request.POST, instance=request.user)
#      p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#      if u_form.is_valid()  and p_form.is_valid():
#          u_form.save()
#          p_form.save()
#          messages.success(request, f'Your account has been Updated!')
#          return redirect('profile') 
#    else:
#      u_form = UserUpdateForm(instance=request.user)
#      p_form = ProfileUpdateForm(instance=request.user.profile)

    

#      context = {
#           'u_form' : u_form,
#           'p_form' : p_form

#      }
#      return render (request, 'users/profile.html', context)




# # message.debug
# # message.info
# # message.success
# # message.warning
# # message.error


#gpt file 
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.core.exceptions import ObjectDoesNotExist

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = None

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            if profile:
                p_form.save()
            else:
                new_profile = p_form.save(commit=False)
                new_profile.user = request.user
                new_profile.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('blog-home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
