from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]