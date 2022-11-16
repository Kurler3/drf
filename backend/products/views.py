from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

# PRODUCT API VIEW
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # FOR DETAILED VIEWS (ONLY 1 ITEM), CAN SPECIFY THE lookup_field, WHICH IS THE KEY OF THAT 1 ITEM
    
    # IN THIS CASE LOOK UP FIELD IS THE PRIMARY KEY (id)
    lookup_field = 'pk'

# CREATE PRODUCT API VIEW
class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # OVERRIDING THE perform_create METHOD ALLOWS TO CHANGE THE DATA BEFORE SAVING
    def perform_create(self, serializer):
        
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)
        # return super().perform_create(serializer)
        
# DELETE PRODUCT API VIEW
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
# UPDATE PRODUCT API VIEW
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
    # PERFORM UPDATE OVERRIDE 
    def perform_update(self, serializer):
        # GET THE INSTANCE
        instance = serializer.save()
        
        if not instance.content:
            instance.content = instance.title

    
# MIXIN GENERIC VIEWS

class ProductMixinView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # GET METHOD
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) 

    
    # POST
    
    # CREATE
    
    
@api_view(['GET', 'POST'])
def product_alt_view(request, pk = None, *args, **kwargs):
    method = request.method
    
    if method == "GET": 
        # GET REQUEST -> DETAIL VIEW OR LIST VIEW
        data = {}
        # IF PASSED PK, THEN RETURN DETAIL VIEW
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
        else:
            # ELSE RETURN LIST VIEW
            queryset = Product.objects.all()
            
            data = ProductSerializer(queryset, many=True).data
        
        return Response(data)
    # IF POST METHOD
    elif method == "POST":
        # CREATE ITEM!!

        # INIT SERIALIZER WITH REQUEST DATA
        serializer = ProductSerializer(data=request.data)
        
        # VALIDATE
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)
            # RETURN DATA
            return Response(serializer.data)