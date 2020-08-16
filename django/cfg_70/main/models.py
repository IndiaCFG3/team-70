from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    CATEGORIES = (  
    ('1', 'IT'),
    ('2', 'Operation'),
    ('3', 'HR'),
    ('4', 'Audit'),
    ('5', 'Account'),
    ('6', 'HOD'),
    ('7', 'Admin'),
    ('8', 'ENC'),
)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=9, choices=CATEGORIES)

    def __str__(self):
        return self.user.username

class Employee(models.Model):
    name = models.CharField(max_length=30)
    center_name = models.CharField(max_length=30)
    region_code = models.CharField(max_length=30)
    grade =  models.CharField(max_length=30)
    date_of_join = models.DateField()
    salary = models.IntegerField()
    mobile_no = models.CharField(max_length=10)
    email_id = models.EmailField(max_length = 254)

    def __str__(self):
        return self.name

