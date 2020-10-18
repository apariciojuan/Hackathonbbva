from django.urls import path
from .views import *
from rest_framework import generics
from rest_framework.routers import DefaultRouter

urlpatterns = [
   path('v1/usuario/', PerfilViewCreate.as_view()),
   path('v1/usuario/<int:pk>/', PerfilView.as_view()),
   path('v1/chequeo/facial/', BioFaceView.as_view()),
]
