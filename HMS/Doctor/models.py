from django.db import models
from User.models import User

# Create your models here.
class Doctor(User):
    doctorID = models.AutoField(primary_key=True, default=1)
    specialization = models.CharField(max_length=100)



