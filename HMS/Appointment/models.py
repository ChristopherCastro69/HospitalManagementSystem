from django.db import models
from HMS.Doctor.models import Doctor
from HMS.Patient.models import Patient

# Create your models here.
class Appointment(models.Model):
    appointmentID = models.AutoField(primary_key=True)
    appointmentDate = models.DateField()
    appointmentTime = models.TimeField()
    doctorID = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)


