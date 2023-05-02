from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

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


# API Routes
# noinspection PyUnresolvedReferences
urlpatterns += [
    path(
        f"{settings.API_PREFIX}/car/",
        include(f"car_app.api.{settings.API_VERSION}.urls", "car-api"),
    ),
    path(
        f"{settings.API_PREFIX}/user/",
        include(f"user_app.api.{settings.API_VERSION}.urls", "user-api"),
    ),
]

# Swagger
urlpatterns += [
    path(f"{settings.API_PREFIX}/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        f"{settings.API_PREFIX}/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
