from django.db import models

# Create your models here.
class Prescription(models.Model):
    prescriptionID = models.AutoField(primary_key=True)
    medicationName = models.CharField(max_length=30)
    dosage = models.FloatField()
    frequency = models.FloatField()
    startDate = models.DateField()
    endDate = models.DateField()
    

