from django.urls import path,include
from .views import index,SingleMenuItemView,MenuItemView,BookingViewSet

urlpatterns = [
    path('',index,name = 'home'),
    path('menu/<int:pk>',SingleMenuItemView.as_view()),
    path('menu/',MenuItemView.as_view()),
]