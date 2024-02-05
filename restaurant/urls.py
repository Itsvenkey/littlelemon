from django.urls import path
from .views import index,SingleMenuItemView,MenuItemView

urlpatterns = [
    path('',index,name = 'home'),
    path('menu/<int:pk>',SingleMenuItemView.as_view()),
    path('menu/',MenuItemView.as_view()),
]