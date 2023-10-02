from django.db import models
from User.models import User


# Create your models here.
class Patient(User):
    patientID = models.AutoField(primary_key=True)
    patientType = models.CharField(max_length=1, choices=(("R", "Resident"), ("O", "Outpatient")), default="R")


class Resident(Patient):
    roomNumber = models.CharField(max_length=5)


class Outpatient(Patient):

