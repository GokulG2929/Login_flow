from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=50)
    mobile_number=models.BigIntegerField()
    user_id=models.IntegerField(null=True)
    location=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=True,null=True)
    modified_date=models.DateTimeField(auto_now=True,null=True)




