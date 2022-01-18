from django.urls import path
from Users import views
#from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import ChangePasswordView


urlpatterns = [
    path('register/', views.register.as_view(),name='register'),
    #path('login/',obtain_auth_token,name='login'),
    path('hello/', views.HelloView.as_view(),name='hello'),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path('api/token/verify/',jwt_views.TokenVerifyView.as_view(),name='token_verify'),
    path('change-password/',ChangePasswordView.as_view(), name='change-password'),
    
    
]
