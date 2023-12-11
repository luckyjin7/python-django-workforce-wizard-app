from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add", views.add, name="add"),
    path("edit/<int:user_id>", views.edit, name="edit"),
    path("udpate/<int:user_id>", views.update, name="update"),
    path("delete/<int:user_id>", views.delete, name="delete"),
]