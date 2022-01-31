from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from common.base_response import set_success_response

@api_view(['GET'])
def healthcheck(request, *args, **kwargs):
    data = set_success_response()
    return Response({"aw": "aw"}, status=200)
