from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
]

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
