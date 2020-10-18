from .serializers import *

from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

import face_recognition


class PerfilViewCreate(generics.CreateAPIView):
    serializer_class = PerfilCreateSerializer


class PerfilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilSerializer


class BioFaceView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            serializer = BioFaceSerializer(data=request.data)
            if serializer.is_valid():
                image = request.data['image']
                numero_usuario = request.data['numero_usuario']
                usuario = PerfilUsuario.objects.get(numero_usuario=numero_usuario)
                known_image = face_recognition.load_image_file(usuario.photo)
                unknown_image = face_recognition.load_image_file(image)

                biden_encoding = face_recognition.face_encodings(known_image)[0]
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

                results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
                #print(results)
                if results[0]:
                    mensaje = "ok"
                else:
                    mensaje = "ko"
                return Response({"result": mensaje}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"result": 'error desconocido'}, status=status.HTTP_400_BAD_REQUEST)