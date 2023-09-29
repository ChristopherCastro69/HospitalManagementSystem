from django.db import models

# Create your models here.
class User(models.Model):
    type = (('D', 'Doctor'), ('P', 'Patient'))
    genderType = (('M', 'Male'), ('F', 'Female'), ('O', 'Prefer not to say'))
    username = models.CharField(max_length=20, null=False, primary_key=True)
    password = models.CharField(max_length=20, null=False)
    firstName = models.CharField(max_length=20, null=False)
    lastName = models.CharField(max_length=20, null=False)
    age = models.IntegerField(null=False, default=20)
    emailAddress = models.CharField(max_length=100, null=False, default="johndoe@gmail.com")
    phoneNumber = models.CharField(max_length=11)
    type = models.CharField(max_length=1, choices=type, default='S')


