# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path("", views.apiOverview, name="apiOverview"),
    path("product-list/", views.showAllProducts, name="product-list"),
    path("product/<int:pk>", views.showOneProduct, name="product"),
    path("create-product/", views.createProduct, name="create-product"),
    path("update-product/<int:pk>", views.updateProduct, name="update-product"),
    path("delete-product/<int:pk>", views.deleteProduct, name="delete-product")

]
