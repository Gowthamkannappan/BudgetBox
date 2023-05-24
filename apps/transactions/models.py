from django.db import models
from apps.users.models import User
from apps.category.models import Category
# Create your models here.

status = (
    ("Income", "Income"),
    ("Expense", "Expense"),
    
)

class Transaction(models.Model):
    class Meta(object):
        db_table='transaction'
    name=models.CharField(
        "Transaction",blank=False,null=False,max_length=200
    )
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    type=models.CharField(
        "Type",max_length=50,blank=False,null=False, choices=status
    )
    
    amount=models.IntegerField(
        "Amount",blank=False,null=False
    )
    
    date=models.DateField(
        "Date", blank=False,null=False,auto_now=True
    )
    
    created_at=models.DateTimeField(
            "Created At", blank=False,null=False,auto_now_add=True
        )
    
    updated_at=models.DateTimeField(
            "Updated At", blank=False,null=False,auto_now=True
        )
    
    def __str__(self):
        return self.name