from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .models import Menu
from .serializers import MenuSerializer
# Create your views here.
def index(reqeust):
    return render(reqeust,'restaurant/index.html',{})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer