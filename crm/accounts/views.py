from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from accounts.decorators import admin_only, allowed_users, unauthenticated_user
from .models import Order, Customer, Products
from .forms import CustomerForm, OrderForm, CreateUserForm
from .filters import OrderFilter
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user = user,
                )

            messages.success(request, 'Account was created for ' + username)
            
            return redirect('login')
        else:
            for error in form.errors:
                messages.error(request, f"{error}: {form.errors[error]}") 

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect') 

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    print('ORDERS:', orders)
    context = {'orders': orders,
               'total_orders':total_orders,
                'delivered': delivered,
                'pending': pending,
               }
    return render(request, "accounts/user.html", context)

@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
    }

    return render(request, "accounts/dashboard.html", context)

def about(request):
    return HttpResponse('About Page')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter
    }

    return render(request, "accounts/customer.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    context = {'form': form}
    return render(request, 'accounts/account_settings.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Products.objects.all()
    return render(request, "accounts/products.html", {'products': products})
@login_required(login_url='login')
def create_order(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    form = OrderForm(initial={'customer': customer})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer', pk=customer.id)

    context = {'form': form, 'customer': customer}
    return render(request, 'accounts/order_form.html', context)
@login_required(login_url='login')
def update_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('customer', pk=order.customer.id)

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)
@login_required(login_url='login')
def delete_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('customer', pk=order.customer.id)

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
