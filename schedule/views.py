from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # <--- AuthenticationForm যুক্ত করুন
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Route

# all route list
def route_list(request):
    routes = Route.objects.all()
    return render(request, 'schedule/route_list.html', {'routes': routes})

# route detail view
def route_detail(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    return render(request, 'schedule/route_detail.html', {'route': route})

# (Sign Up) View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # অ্যাকাউন্ট তৈরির পরেই অটোমেটিক লগইন করিয়ে দেবে
            return redirect('route_list')
    else:
        form = UserCreationForm()
    return render(request, 'schedule/register.html', {'form': form})

# (Log In) View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('route_list')
    else:
        form = AuthenticationForm()
    return render(request, 'schedule/login.html', {'form': form})

# (Log Out) View
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('route_list')