from rest_framework.views import APIView
from .serializers import CartSerializer
from rest_framework.response import Response
from .models import ShoppingCart
# Create your views here.


class GetCartView(APIView):
    def get(self, request):
        print("User ", request.session["userID"])
        cart_data = ShoppingCart.objects.filter(user=request.session["userID"])
        print(cart_data)
        if cart_data.count()>1:
            serializer = CartSerializer(cart_data, many=True)
        else:
            serializer = CartSerializer(cart_data)
        return Response(serializer.data)
    def post(self, request):
        item = request.data["item"]
        quantity = request.data["quantity"]
        ShoppingCart.objects.create(user=request.session["userID"], item=item, quantity=quantity)
        return Response({"Success":"Success"}, status=200)
