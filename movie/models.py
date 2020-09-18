from django.db import models

from bottle.models import User
from common.models import Base
from movie.constants import user_watch_list_choices


class Movies(Base):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    movie_rating = models.SmallIntegerField()


class UserWatchList(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=user_watch_list_choices)

    class Meta:
        unique_together = [
            ['user', 'movie']
        ]


class UserRating(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()

    class Meta:
        unique_together = [
            ['user', 'movie']
        ]
