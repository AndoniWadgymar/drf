from rest_framework import viewsets, mixins


from products.models import Product
from products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
  """
  get -> list -> Queryset
  get -> retrieve -> Product Instancce Detail View
  post -> create -> New Instance
  put -> Update
  patch -> Partial Update
  delete -> destroy
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

class ProductGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
  """
  get -> list -> Queryset
  get -> retrieve -> Product Instancce Detail View
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'