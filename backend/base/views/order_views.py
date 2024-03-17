from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Product, Order, OrderItem, ShippingAddress
from backend.base.serializers import ProductSerializer

from rest_framework import status
from datetime import datetime


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    return Response("ORDER")
