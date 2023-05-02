from django.urls import path

from user_app.views import login_view, logout_view, signup_view

app_name = "user_app"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
]
