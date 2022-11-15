from rest_framework import generics

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
        
# LIST API VIEW
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
def product_alt_view(request, *args, **kwargs):
    method = request.method
    
    if method == "GET": 
        # GET REQUEST -> DETAIL VIEW OR LIST VIEW
        pass
        # GET URL ARGS

        # IF PASSED PK, THEN RETURN DETAIL VIEW
        
        # ELSE RETURN LIST VIEW
        
    # IF POST METHOD
    elif method == "POST":
        # CREATE ITEM!!

        # INIT SERIALIZER WITH REQUEST DATA
        pass
        