from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=47)
    description = models.CharField(widgets=models.TextField,blank=True,default='')
    image = models.ImageField(upload_to='group_images',blank=True)
    members = models.ManyToManyField(to=User,through='GroupMember')

    # def get_absoulte_url(self):
    #     return reverse('groups:single')

    class Meta:
        ordering=['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='members')
    user = models.ForeignKey(User,related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        constraints = [ # to maintain user only once in group group and user combo should be unique
            models.UniqueConstraint(fields=['group', 'user'], name='uniqueuseringroup')
        ]
