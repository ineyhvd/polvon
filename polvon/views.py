from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView

# Create your views here.

# def home(request):
#     return render(request,'home.html')
#
# def details(request):
#     return render(request,'detail.html')

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, Product
from .pagination import CustomLimitOffsetPagination
from .permissions import DistrictPermission , TimeDistrictPermission
from .serializers import CommentSerializer, DistrictSerializer, ProductSerializer
from polvon import pagination


class CommentListCreateView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return None

    def get(self, request, pk):
        comment = self.get_object(pk)
        if comment is None:
            return Response({"error": "Izoh topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        comment = self.get_object(pk)
        if comment is None:
            return Response({"error": "Izoh topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        if comment is None:
            return Response({"error": "Izoh topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        comment.delete()
        return Response({"message": "Izoh o‘chirildi"}, status=status.HTTP_204_NO_CONTENT)


class DistrictView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Comment.objects.all()
    permission_classes = (DistrictPermission,)

class TimeDistrictView(RetrieveUpdateAPIView):
    serializer_class = DistrictSerializer
    queryset = Comment.objects.all()
    permission_classes = (TimeDistrictPermission,)

class ProductView(APIView):
    pagination_class = CustomLimitOffsetPagination
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





