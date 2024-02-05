from django.urls import path,include
from .views import index,SingleMenuItemView,MenuItemView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('',index,name = 'home'),
    path('menu/<int:pk>',SingleMenuItemView.as_view()),
    path('menu/',MenuItemView.as_view()),
    path('api-token-auth/',obtain_auth_token)
]