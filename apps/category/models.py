from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta(object):
        db_table='category'
    name=models.CharField(
        "Category Name", blank=False,null=False,max_length=200
    )
    color_code=models.CharField(
        "Color Code", blank=False,null=False,max_length=50
    )
    created_at=models.DateTimeField(
        "Created At", blank=False,null=False,auto_now_add=True
    )
    updated_at=models.DateTimeField(
        "Updated At", blank=False,null=False,auto_now=True
    )
    def __str__(self):
        return self.name
    