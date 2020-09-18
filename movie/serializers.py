from rest_framework.serializers import ModelSerializer

from movie.models import Movies


class MovieListSerializer(ModelSerializer):

    class Meta:
        model = Movies