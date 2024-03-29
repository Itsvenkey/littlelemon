from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .models import Menu,Booking,MenuItem
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(reqeust):
    return render(reqeust,'restaurant/index.html',{})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer