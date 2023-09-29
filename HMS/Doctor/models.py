from django.db import models
from User.models import User

# Create your models here.
class Doctor(User):
    doctorID = models.AutoField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)



