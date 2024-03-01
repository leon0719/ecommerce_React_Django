from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


urlpatterns = [
    path("api/users/login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api", views.getRoutes, name="routes"),
    path("api/products", views.getProducts, name="products"),
    path("api/product/<str:pk>", views.getProduct, name="product"),
    path("", views.hello, name="hello"),
]
