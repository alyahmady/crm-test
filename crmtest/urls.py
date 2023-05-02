from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

from crmtest.views import home_view, perform_healthcheck

# Admin
urlpatterns = [
    path("admin/", admin.site.urls),
]

# Health Check
urlpatterns += [path("healthcheck/", perform_healthcheck, name="health-check")]

# MVC Site
urlpatterns += [
    path("", home_view, name="home"),
    path("user/", include("user_app.urls")),
    path("car/", include("car_app.urls")),
    path("rental/", include("rental_app.urls")),
]

# API Routes

# Static and Media
urlpatterns += [
    re_path(
        route=r"^media/(?P<path>.*)$",
        view=serve,
        kwargs={
            "document_root": settings.MEDIA_ROOT,
        },
    ),
    re_path(
        route=r"^static/(?P<path>.*)$",
        view=serve,
        kwargs={
            "document_root": settings.STATIC_ROOT,
        },
    ),
]
