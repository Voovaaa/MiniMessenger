from django.contrib import admin
from django.urls import path
from mini_messenger import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("1231", views.hello_world, name="h")
]
