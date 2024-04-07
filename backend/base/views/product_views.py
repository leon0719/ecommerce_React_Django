from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Product
from base.serializers import ProductSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import status


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


@api_view(["POST"])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user
    product = Product.objects.create(
        user=user,
        name="Sample Name",
        price=0,
        brand="Sample Brand",
        countInStock=0,
        category="Sample Category",
        description="",
    )
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)  # SELECT * FROM product WHERE id = pk;

    product.name = data["name"]
    product.price = data["price"]
    product.brand = data["brand"]
    product.countInStock = data["countInStock"]
    product.category = data["category"]
    product.description = data["description"]

    product.save()  # UPDATE product SET ...;

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])  # only admin can delete product
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)  # SELECT * FROM product WHERE id = pk;
    product.delete()
    return Response("Producte Deleted")


@api_view(["POST"])
def uploadImage(request):
    data = request.data
    product_id = data["product_id"]
    product = Product.objects.get(_id=product_id)
    product.image = request.FILES.get("image")
    product.save()
    return Response("Image was uploaded", status=status.HTTP_201_CREATED)


@api_view(["GET"])
def hello(request):
    return Response("Hello Django")
