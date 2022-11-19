from rest_framework import generics, mixins, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

# PRODUCT API VIEW
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # AUTHENTICATION
    authentication_classes = [authentication.SessionAuthentication]
    
    # PERMISSIONS
    permission_classes = [permissions.DjangoModelPermissions]        

    # FOR DETAILED VIEWS (ONLY 1 ITEM), CAN SPECIFY THE lookup_field, WHICH IS THE KEY OF THAT 1 ITEM
    
    # IN THIS CASE LOOK UP FIELD IS THE PRIMARY KEY (id)
    lookup_field = 'pk'

# CREATE PRODUCT API VIEW
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # AUTHENTICATION
    authentication_classes = [authentication.SessionAuthentication]
    
    # PERMISSIONS
    permission_classes = [permissions.DjangoModelPermissions]
    
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
    # AUTHENTICATION
    authentication_classes = [authentication.SessionAuthentication]
    
    # PERMISSIONS
    permission_classes = [permissions.DjangoModelPermissions]
# UPDATE PRODUCT API VIEW
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    # AUTHENTICATION
    authentication_classes = [authentication.SessionAuthentication]
    
    # PERMISSIONS
    permission_classes = [permissions.DjangoModelPermissions]
    # PERFORM UPDATE OVERRIDE 
    def perform_update(self, serializer):
        # GET THE INSTANCE
        instance = serializer.save()
        
        if not instance.content:
            instance.content = instance.title

    
# MIXIN GENERIC VIEWS

class ProductMixinView(
    # INHERITS FROM THE DESTROY MODEL MIXIN (self.delete)
    mixins.DestroyModelMixin,
    # INHERITS FROM THE UPDATE MODEL MIXIN (self.update)
    mixins.UpdateModelMixin,
    # INHERITS FROM THE CREATE MODEL MIXIN (self.create)
    mixins.CreateModelMixin,
    # INHERITS FROM LIST MODEL MIXIN (self.list)
    mixins.ListModelMixin,
    # INHERITS FROM RETRIEVE MODEL MIXIN (self.retrieve)
    mixins.RetrieveModelMixin,
    # INHERITS FROM THE GENERIC API VIEW
    generics.GenericAPIView,
):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # DEFINING THE LOOK UP FIELD (FIELD THAT IT WILL QUERY ON FOR THE DETAILED/UPDATE/DELETE VIEW)
    # BY DEFAULT THIS IS THE PRIMARY KEY (pk)
    lookup_field = "pk"
    
    # GET METHOD
    def get(self, request, *args, **kwargs):
        # HERE CAN GET THE PK FROM THE URL INSTEAD OF DEFINING IT IN THE ARGUMENTS
        pk = kwargs.get('pk')

        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs) 
    # CREATE
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs);
    # UPDATE
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    # DELETE
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
    
    # OVERRIDING THE perform_create METHOD ALLOWS TO CHANGE THE DATA BEFORE SAVING
    def perform_create(self, serializer):
        
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        
        if content is None:
            content = title
            
        serializer.save(content=content)
    
    
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