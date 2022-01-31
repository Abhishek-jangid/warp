from statistics import mode
from django.db import models

from common.models import BaseModel

# Create your models here.

class User(BaseModel):
    email = models.CharField(
        max_length=55, null=False, blank=False, unique=True, db_index=True)
    mobile = models.CharField(
        max_length=10, null=False, blank=False, unique=True, db_index=True)
    first_name = models.CharField(max_length=40, null=False, blank=False, unique=True)
    last_name = models.CharField(max_length=40, null=False, blank=False, unique=True)

    class Meta:
        db_table = 'users'
