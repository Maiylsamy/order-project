from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.IntegerField(default=0)

    role_choices=(
        (0,'admin'),
        (1,'manager'),
        (2,'employee'),
    )
    role = models.IntegerField(default=0,choices=role_choices)