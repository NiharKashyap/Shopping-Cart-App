from django.http import HttpResponse
from rest_framework.views import APIView
from api.serializers import CartSerializer
from rest_framework.response import Response
from api.models import ShoppingCart
from rest_framework.decorators import api_view
from .decorators import user_token_athenticated
# Create your views here.


class GetCartView(APIView):

    def get(self, request):
        print("User ", request.session["userID"])
        cart_data = ShoppingCart.objects.filter(user=request.session["userID"])
        cart_serializer = CartSerializer(cart_data, many=True)
        return Response(cart_serializer.data)
    
    @user_token_athenticated
    def post(self, request):
        item = request.data["item"]
        quantity = request.data["quantity"]
        ShoppingCart.objects.create(user=request.session["userID"], item=item, quantity=quantity)
        return Response({"Success":"Success"}, status=200)

# @decorator_from_middleware(TestMiddleware)

@api_view(["GET"])
@user_token_athenticated
def without_header(request):
    print("Without Header but passed")
    return HttpResponse("Par hoi golu")
    
