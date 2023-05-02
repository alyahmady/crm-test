from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from user_app.forms import LoginForm, SignUpForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()

    return render(request, "user_app/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'user_app/signup.html', {'form': form})
