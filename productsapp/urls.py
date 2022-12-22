from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("details/<int:pk>", views.details, name="details"),
    path("add-product", views.addproduct, name='add-product'),
    path("update/<int:pk>", views.update , name="update"),
    path("delete/<int:pk>", views.delete, name="delete")
]