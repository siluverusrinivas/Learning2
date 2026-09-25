from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterView(APIView):

    def post(self, request):
        print(request.data)

        return Response(
            {"message": "Data received successfully"},
            status=status.HTTP_200_OK
        )

    def get(self, request):
        users = Register.objects.all()

        serializer = RegisterSerializer(users, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
