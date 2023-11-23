from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Customers, LoginView, LogoutView, RegisterView

router = DefaultRouter()
router.register('', Customers)

urlpatterns = [     
    path('register/',RegisterView.as_view(), name='register' ),           
    path('login/',LoginView.as_view(), name='login' ),
    path('logout/',LogoutView.as_view(), name='logout' ),
    path('', include(router.urls)),
]
