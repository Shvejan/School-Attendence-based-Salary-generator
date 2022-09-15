from django.db import models

# Create your models here.

def id_generator():
     count = employee.objects.all().count()
     return 'NN'+str(1001+count)

class employee(models.Model):
    id =  models.CharField(primary_key=True,default=id_generator,max_length=100)
    bank=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    pan=models.CharField(max_length=100)
    accNo=models.BigIntegerField()
    pfNo=models.CharField(max_length=100)
    esiNo=models.CharField(max_length=100)
    uan=models.CharField(max_length=100)
    leaves_allowed=models.IntegerField(default=3)
    join_date=models.DateField()
    basic=models.IntegerField()
    sa=models.IntegerField(default=0)
    ca=models.IntegerField(default=0)
    ma=models.IntegerField(default=0)


    def __str__(self):
        return self.name
