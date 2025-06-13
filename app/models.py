from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class todo(models.Model):
    srno=models.AutoField(primary_key=True,auto_created=True)
    title=models.CharField(max_length=20)
    date=models.DateField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
