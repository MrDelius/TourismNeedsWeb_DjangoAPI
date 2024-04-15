"""
URL configuration for findhotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotels import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.UserRegistrationAPIView.as_view(), name='user_registration'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/needs/', views.NeedListCreateView.as_view(), name='need-list'),
    path('api/needs/<int:pk>/', views.NeedDetailView.as_view(), name='need-detail'),
    path('api/userprofiles/<int:pk>/', views.UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('api/users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]
