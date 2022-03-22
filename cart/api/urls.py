from django.urls import path
from .views import GetCartView, without_header

urlpatterns = [
    path('get_cart', GetCartView.as_view()),
    path('head', without_header)
]