from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts')
    created_time = models.DateTimeField(auto_now=True)
    message = models.CharField(widgets=models.TextField)
    group = models.ForeignKey(Group,related_name='groupposts',null=True,blank=True)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk})

    class Meta:
        Ordering = ['-created_time']