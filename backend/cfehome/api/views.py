from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#   """
#   DRF API VIEW
#   """
#   instance = Product.objects.all().order_by("?").first()
#   data = {}
#   if instance:
#     # data = model_to_dict(model_data, fields=['id', 'title', 'price']) #clean and easy conversion
#     data = ProductSerializer(instance).data

#   return Response(data)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
  """
  DRF API VIEW
  """
  serializer = ProductSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    # instance = serializer.save()
    print(serializer.data)
    data = serializer.data
    return Response(data)
  return Response({"invalid": "Not good data"}, status=400)