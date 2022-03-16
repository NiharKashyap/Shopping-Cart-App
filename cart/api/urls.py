from django.urls import path
from .views import GetCartView

urlpatterns = [
    path('get_cart', GetCartView.as_view())
]