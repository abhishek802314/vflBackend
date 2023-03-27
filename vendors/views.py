from django.shortcuts import render
from rest_framework import generics, permissions, status, filters
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VendorViewSerializer, VendorListSerializer, VendorSpecificListSerializer, VendorCreateSerializer
from .models import Vendor
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend


class VendorView(generics.GenericAPIView):
    serializer_class = VendorViewSerializer
    permission_classes = [permissions.AllowAny,]

        
    def get(self, request, pk):
        vendor = Vendor.objects.get(pk=pk)
        
        serializer = self.get_serializer(vendor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        pass

    def patch(self, request, pk):
        vendor = Vendor.objects.get(pk=pk)
        print(vendor.creator)
        print(self.request.user)
        if (vendor.creator == self.request.user):
            serailizer = VendorViewSerializer(vendor, data=request.data, partial=True)
            if serailizer.is_valid():
                serailizer.save()
                return Response(serailizer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, pk):
        pass


class VendorCreateView(generics.GenericAPIView):
    serializer_class = VendorCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
class VendorListView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorListSerializer

    def get(self, request):
        queryset = Vendor.objects.all()
        response = self.get_serializer(queryset, many=True)
        return Response(response.data, status=status.HTTP_200_OK)

    # def get_queryset(self):
    #     city = self.request.query_params.get('city')
    #     products= self.request.query_params.get('products')
    #     queryset = Vendor.objects.filter(city__iexact = city,products__icontains = products)
    #     return queryset
    
class VendorSpecificListView(generics.ListAPIView):
    serializer_class = VendorListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = Vendor.objects.filter(creator = request.user)
        response = self.get_serializer(queryset, many=True)
        return Response(response.data, status.HTTP_200_OK)
            
