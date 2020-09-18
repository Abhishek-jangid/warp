from django.db import models

from common.models import Base


class User(Base):
    mobile = models.CharField(unique=True, max_length=10)
    email = models.EmailField(unique=True, max_length=10)
    pan_number = models.EmailField(unique=True, max_length=10)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    last_login = models.DateField()
    date_joined = models.DateField(auto_now_add=True)

    @classmethod
    def get_user_with_mobile(cls, mobile):
        return cls.objects.get(mobile=mobile)

    @classmethod
    def get_user_with_email(cls, email):
        return cls.objects.get(email=email)

    @classmethod
    def get_user_with_pan_number(cls, pan_number):
        return cls.objects.get(pan_number=pan_number)

    @classmethod
    def run():
        pass
