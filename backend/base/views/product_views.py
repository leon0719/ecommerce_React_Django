from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Product, Review
from base.serializers import ProductSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
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


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createProductReview(request, pk):
    user = request.user

    try:
        product = Product.objects.get(_id=pk)
    except Product.DoesNotExist:
        return Response(
            {"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

    data = request.data
    rating = data.get("rating")
    comment = data.get("comment")

    if not rating:
        return Response(
            {"detail": "Please provide a rating"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not (1 <= rating <= 5):
        return Response(
            {"detail": "Rating must be between 1 and 5"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if Review.objects.filter(user=user, product=product).exists():
        return Response(
            {"detail": "Product already reviewed"}, status=status.HTTP_400_BAD_REQUEST
        )

    Review.objects.create(
        user=user,
        product=product,
        name=user.first_name,
        rating=rating,
        comment=comment,
    )

    reviews = product.review_set.all()
    num_reviews = reviews.count()
    total_rating = sum(review.rating for review in reviews)
    product.numReviews = num_reviews
    product.rating = total_rating / num_reviews
    product.save()

    return Response({"detail": "Review Added"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def hello(request):
    return Response("Hello Django")
