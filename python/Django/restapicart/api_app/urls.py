from django.urls import path
from .views import CartView

urlpatterns = [
    path('shopping/', CartView.as_view()),
    path('shopping/<str:pk>', CartView.as_view())
]