from django.db import models
from django.contrib.auth import models as usermodels

# Create your models here.
class User(usermodels.User,usermodels.PermissionsMixin):
    def __str__(self):
        return self.username # As we have inherited User model, we can use its fieldname using self

