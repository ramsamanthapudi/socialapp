from django.contrib.auth.forms import UserCreationForm
from django.forms import Form
from .models import User


class UserChereForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username', 'email', 'password1', 'password2')


