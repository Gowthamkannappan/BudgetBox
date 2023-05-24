from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class User(models.Model):
    class Meta(object):
        db_table='user'
    name = models.CharField(
        'Name', blank=False,null=False,max_length=255
    )
    email = models.CharField(
        'Email', blank=False,null=False,max_length=255
    )
    password=models.CharField(
        "Password", blank=False,null=False,max_length=255
    )
    budget= models.IntegerField(
        "Budget", blank=False,null=False,default=0
    )
    profile =CloudinaryField(
        "Profile Image", blank=True,null=True
    )
    token= models.CharField(
        'Token',blank=False,null=False,max_length=500
    )
    token_expires=models.DateTimeField(
        "Token Expires", blank=False,null=False
    )
    created_at=models.DateTimeField(
        "Created_At",blank=False, auto_now_add=True
    )
    updated_at=models.DateTimeField(
        "Updated_At",blank=False, auto_now=True
    )
    def __str__(self):
        return self.name