from django.db import models

# Create your models here.
class department(models.Model):
    id = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=100 , null=False)
    location=models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.id, self.name}'
    
    
class role(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, null = False)
    
    
    def __str__(self):
        return self.id, self.name
    
    
class employee(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100)
    dept = models.ForeignKey(department,on_delete=models.CASCADE, related_name="employee")
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(role, on_delete=models.CASCADE,related_name="employee")
    phone = models.CharField(null=True, max_length=15)
    hire_date = models.DateField()
    
    
    def __str__(self):
        # return "%s %s %s" %(self.firstname, self.lastname, self.phone)
        return self.firstname, self.lastname, self.phone
    
    
