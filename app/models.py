from django.db import models
from datetime import datetime

# Create your models here.

class Locality(models.Model):
    pincode = models.IntegerField(primary_key=True)
    hospital_count = models.IntegerField(default=0)
    case_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pincode)

class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    pincode = models.ForeignKey(Locality,on_delete=models.PROTECT)
    patient_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,default="John Doe")
    address = models.CharField(max_length=256)
    age = models.IntegerField()
    hospital_id = models.ForeignKey(Hospital,on_delete=models.PROTECT)
    gender = models.CharField(max_length=15)
    test_status = models.CharField(max_length=3)

    def __str__(self):
        return str(self.id)


class Quarantine_Info(models.Model):
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE,primary_key=True)
    address = models.CharField(max_length=256)
    test_status = models.CharField(max_length=3)

    def __str__(self):
        return str(self.patient_id)

class Close_Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,default="John Doe")
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    relation = models.CharField(max_length=256)
    age = models.IntegerField()
    gender = models.CharField(max_length=15)
    address = models.CharField(max_length=256)
    test_status = models.CharField(max_length=3)

    def __str__(self):
            return str(self.id)
