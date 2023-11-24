from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import RegistrationForm


def sign(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registapp/sign.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def logout_view(request):

    logout = LogoutView.as_view(next_page='login')
    return logout(request)
