# from django.http import JsonResponse, HttpResponse
import json
from rest_framework.response import Response

from rest_framework.decorators import api_view

# IMPORT PRODUCT MODEL
from products.models import Product
from django.forms.models import model_to_dict


@api_view(["GET", "POST"])
def api_home(req, *args, **kwargs):
    # MAKES A RANDOM QUERY SET (RANDOMNLY CHOOSES A PROPERTY TO ORDER BY AND GETS THE FIRST ITEM OF THAT ARRAY
    model_data = Product.objects.all().order_by("?").first()

    # INIT DATA
    data = {}

    # IF FOUND A PRODUCT
    if model_data:
        # MODEL -> PYTHON DICT -> JSON FOR CLIENT
        data = model_to_dict(model_data)

    return Response(data)