from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Shoppingcart
from .serializers import Cartserializer
from rest_framework import status

# Create your views here.
class CartView(APIView):
    def get(self, request, pk=None):
        if pk != None:
            item = Shoppingcart.objects.get(id=pk)
            serializer = Cartserializer(item)
            return Response({"status":"Success", "data" : serializer.data}, status=status.HTTP_200_OK)

        else:
            shoppingcarts = Shoppingcart.objects.all()
            serializer = Cartserializer(shoppingcarts, many=True)
            return Response({"status":"Success", "data" : serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Cartserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "Success", "data" : serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response({"status" : "Request failed", "data" : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        item = get_object_or_404(Shoppingcart, id=pk)
        item.delete()
        return Response({"status" : "Success", "data" : "Item deleted"}, status=status.HTTP_200_OK)


    def put(self, request, pk=None):
        item = Shoppingcart.objects.get(id=pk)
        serializer = Cartserializer(item, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "Success", "data" : serializer.data}, status=status.HTTP_200_OK)
        else: 
            return Response({"status" : "Request failed", "data" : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)