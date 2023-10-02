from django.db import models
from HMS.Patient.models import Patient
from HMS.Doctor.models import Doctor

# Create your models here.
class Prescription(models.Model):
    prescriptionID = models.AutoField(primary_key=True)
    medicationName = models.CharField(max_length=30)
    dosage = models.FloatField()
    frequency = models.FloatField()
    startDate = models.DateField()
    endDate = models.DateField()
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
