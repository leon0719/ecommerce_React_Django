from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Product
from .serializer import ProductSerializer, UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.


# 用於設定 payload 資訊
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


# 用於轉成 Json 格式
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "/api/products",
        "/api/products/create/",
        "/api/products/upload/",
        "/api/products/<id>/reviews/",
        "/api/products/top/",
        "/api/products/<id>/",
        "/api/products/delete/<id>/",
        "/api/products/<update>/<id>",
    ]
    return Response(routes)


@api_view(["GET"])
@permission_classes([IsAuthenticated])  # restrict(限制)權限
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def hello(request):
    return Response("Hello Django")
