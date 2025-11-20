from .models import Orderitem
from rest_framework import viewsets
from .serializer import  OrderitemSerializer

class OrderitemViewSet(viewsets.ModelViewSet):
    queryset = Orderitem.objects.all()
    serializer_class = OrderitemSerializer