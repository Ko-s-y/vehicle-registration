from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status
from .serializers import UserSerializer, SegmentSerializer, BrandSerializer, VehicleSerializer
from .models import Segment, Brand, Vehicle
from rest_framework.response import Response

class CreateUserView(generics.CreateAPIView):
  serializer_class = UserSerializer
  permission_classes = (permissions.AllowAny,)

class ProfileUserView(generics.RetrieveUpdateAPIView):
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user

  def update(self, request, *args, **kwargs):
    response = {'message': 'PUT method is not allowed'}
    return Response(response, status=status.HTP_405_METHOD_NOT_ALLOWED)

  def partial_update(self, request, *args, **kwargs):
    response = {'message': 'PATCH method is not allowed'}
    return Response(response, status=status.HTP_405_METHOD_NOT_ALLOWED))
