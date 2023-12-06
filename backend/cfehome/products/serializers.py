from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title, validate_title_no_hello, unique_product_title

class ProductSerializer(serializers.ModelSerializer):
  discount = serializers.SerializerMethodField(read_only=True)
  edit_url = serializers.SerializerMethodField(read_only=True)
  url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
  #We need to set the write only to allow it not to be on the Product model
  # email = serializers.EmailField(write_only=True)

  #If we want to add costum validators from another file we do this
  title = serializers.CharField(validators=[unique_product_title, validate_title_no_hello])
  # Create another field from a source in this case title
  name = serializers.CharField(source='title', read_only=True)

  class Meta:
    model = Product
    fields = [
      'url',
      'edit_url',
      # 'email',
      'name',
      'pk',
      'title',
      'content',
      'price',
      'sale_price',
      'discount',
    ]

  #Costum validation in our serializer
  # def validate_title(self, value):
  #   queryset = Product.objects.filter(title__iexact=value)
  #   if queryset.exists():
  #     raise serializers.ValidationError(f"{value} is already a product name")
  #   return value


  #if we want to add extra details to de serializer and not the model we
  # need to modify the create funct
  # def create(self, validated_data):
  #   return super().create(validated_data)

  # def update(self, instance, validated_data):
  #   return

  def get_edit_url(self, obj):
    request = self.context.get('request')
    if request is None:
      return None
    return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)

  # def get_url(self, obj):
  #   request = self.context.get('request')
  #   if request is None:
  #     return None
  #   return reverse("product-detail", kwargs={"pk":obj.pk}, request=request)

  def get_discount(self,obj):
    if not hasattr(obj, 'id'):
        return None
    if not isinstance(obj, Product):
       return None
    return obj.get_discount()