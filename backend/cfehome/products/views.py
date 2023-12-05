from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from products.models import Product
from products.serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # lookup_field = 'pk

#We can use CREATE just to create with POST or ListCreate to list all and also create
class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

# Used when aditional functions want to be run on create
  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    print(serializer)
    serializer.save()

# We can create a function view that gets details, gets list, and post all in one
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
  method = request.method

  if method == "GET":
    if pk is not None:
      # Detail view
      obj = get_object_or_404(Product, pk=pk)
      data = ProductSerializer(obj, many=False).data
      return Response(data)
    else:
      # List view
      queryset = Product.objects.all()
      data = ProductSerializer(obj, many=True).data
      return Response(data)

  if method == "POST":
    #Create an item
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content') or None
      if content is None:
        content = title
      serializer.save(content=content)
      return Response(serializer.data)
    return Response({"Invalid": "Not good data"}, status=400)