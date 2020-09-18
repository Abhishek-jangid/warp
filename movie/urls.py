from django.urls import path
from movie.views import (
    get_auth_token,
    GetAllMovies
)


urlpatterns = [
    path('get-auth-token/', get_auth_token, name='get_auth_token'),
    path('get-all/', GetAllMovies, name='test_view'),
]
