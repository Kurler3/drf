from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount"
        ]
    def get_my_discount(self, obj):
        
        # IF NO INSTANCE IS ATTACHED TO SERIALIZER
        if not hasattr(obj, 'id'):
            return None
        # CAN ALSO DO IT BY CHECKING IF OBJ IS INSTANCE OF PRODUCT
        # if not isinstance(obj, Product):
        #     return None
        return obj.get_discount()
       