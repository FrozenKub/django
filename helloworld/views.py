from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HelolWorld(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'type': request.query_params.get('id')})

    def post(self, request):
        heh = request.data['heh']
        return Response({'type': heh})