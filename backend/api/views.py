from rest_framework.response import Response

from rest_framework.decorators import api_view

# IMPORT PRODUCT MODEL
from products.models import Product

from products.serializers import ProductSerializer
from django.forms.models import model_to_dict


@api_view(["POST"])
def api_home(req, *args, **kwargs):
    # MAKES A RANDOM QUERY SET (RANDOMNLY CHOOSES A PROPERTY TO ORDER BY AND GETS THE FIRST ITEM OF THAT  ARRA
    # VALIDATE DATA
    serializer = ProductSerializer(data=req.data)
    
    if serializer.is_valid():
        print(serializer.data)
        data = serializer.data
        return Response(data) 
   