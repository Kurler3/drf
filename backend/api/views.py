from rest_framework.response import Response

from rest_framework.decorators import api_view

# IMPORT PRODUCT MODEL
from products.models import Product

from products.serializers import ProductSerializer
from django.forms.models import model_to_dict


@api_view(["POST"])
def api_home(req):    
    # VALIDATE DATA
    serializer = ProductSerializer(data=req.data)
    
    # IF DATA IS VALID 
    if serializer.is_valid(raise_exception=True):
        # SAVE IT
        # instance = serializer.save()

        return Response(serializer.data) 
    else:
        return Response({"invalid": "Invalid data"}, status=400)
   