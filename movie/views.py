from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from movie.models import Movies
from movie.serializers import MovieListSerializer
from movie.user_service import UserService


class GetAllMovies(ListAPIView):
    serializer_class = MovieListSerializer
    permission_classes = [[AllowAny, ], ]

    def get_queryset(self):
        return Movies.objects.all()


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_auth_token(request, *args, **kwargs):
    mobile = request.data.get('mobile', None)
    if not mobile:
        return Response({}, status=status.HTTP_400_BAD_REQUEST, exception=True)
    res_data = UserService(mobile).get_auth_token()
    status_code = status.HTTP_400_BAD_REQUEST
    if res_data['status']:
        status_code = status.HTTP_200_OK
    return Response(res_data, status=status_code)
