from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from biblioteca.models import Autor, Libro
from biblioteca.serializers import AutorSerializer, LibroSerializer
# Create your views here.

#-----------LIBRO---------

@api_view(['POST', 'PUT'])
def crear_libro(request):
    datos_deserializado = LibroSerializer(data=request.data)
    if datos_deserializado.is_valid():
        datos_deserializado.save()
        return Response(datos_deserializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(datos_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_libros(request):
    libros = Libro.objects.all()
    serializer = LibroSerializer(libros, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def modificar_libro(request, id):
    try:
        libro = Libro.objects.get(id=id)
        datos_deserializado = LibroSerializer(libro, data=request.data)
        if datos_deserializado.is_valid():
            datos_deserializado.save()
            return Response(datos_deserializado.data, status=status.HTTP_200_OK)
        else:
            return Response(datos_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)

    except Libro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def eliminar_libro(request, id):
    try:
        libro = Libro.objects.get(id=id)
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)



