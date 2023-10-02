from django.db import models
from Doctor.models import Doctor
from Patient.models import Patient

# Create your models here.
class Appointment(models.Model):
    appointmentID = models.AutoField(primary_key=True)
    appointmentDate = models.DateField(null=True)
    appointmentTime = models.TimeField(null=True)
    doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)


