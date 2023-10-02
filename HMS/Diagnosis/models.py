from django.db import models
from HMS.Patient.models import Patient
from HMS.Doctor.models import Doctor
# Create your models here.
class Diagnosis(models.Model):
    diagnosisID = models.AutoField(primary_key=True)
    diagnosisName = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    dateCreated = models.DateField()
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
