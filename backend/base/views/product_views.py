from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Product
from base.serializers import ProductSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()  # SELECT * FROM product;
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)  # SELECT * FROM product WHERE id = pk;
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])  # only admin can delete product
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)  # SELECT * FROM product WHERE id = pk;
    product.delete()
    return Response("Producte Deleted")


@api_view(["GET"])
def hello(request):
    return Response("Hello Django")
