from django.views.generic import TemplateView
from djvue.views import FileUploadView
from rest_framework import status, viewsets
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .helper_functions import get_score
from .models import Game
from .serializers import CSVUploadSerializer, GameSerializer, HandleUploadSerializer


class HomeTemplateView(TemplateView):
    template_name = "home.html"


class CSVUploadView(FileUploadView):
    serializer_class = CSVUploadSerializer


class HandleUploadView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = HandleUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetScoresView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, **kwargs):
        return Response(get_score())


class GetGamesView(
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Game.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = GameSerializer
