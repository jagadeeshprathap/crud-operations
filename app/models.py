from django.db import models

# Create your models here.
class Dept(models.Model):
    d_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.d_name
class Emp(models.Model):
    d_name=models.ForeignKey(Dept,on_delete=models.CASCADE)
    e_name=models.CharField(max_length=33,primary_key=True)
    e_no=models.IntegerField()
    def __str__(self):
        return self.e_name
class Family(models.Model):
    e_name=models.ForeignKey(Emp,on_delete=models.CASCADE)
    sal=models.IntegerField()
    gender=models.CharField(max_length=21)
    id=models.IntegerField(primary_key=True)
    def __str__(self):
        return self.gender                                          


