from django.shortcuts import render
from rest_framework.views import APIView
from status.models import Status
from .serializers import statusSerializer
from rest_framework.response import Response
# Create your views here.


class all_statuses(APIView):
    def get(self,request):
        all_statuses = Status.objects.all()
        serializer = statusSerializer(all_statuses, many=True)
        return Response(serializer.data)
