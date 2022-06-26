from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class registration(AbstractUser):
    course = [
        ('AT','BET-AT'),
        ('CT','BET-CT'),
        ('CoET','BET-CoET'),
        ('EsET','BET-EsET'),
        ('ET','BET-ET'),
        ('MT','BET-MT'),
        ('PPT','BET-PPT'),
    ]

    userType = [
        ('DIT','Department of Industrial Technology'),
        ('OAA','Office of Academic Affairs'),
        ('OCL','Office of Campus Librarian'),
        ('ORE','Office of Research and Extension'),
        ('Adviser','Thesis Adviser'),
        ('FIC','Subject Teacher'),
        ('ADMIN','Admin'),
    ]
    major = models.CharField(max_length = 10, choices = course, verbose_name = 'major')
    idNumber = models.IntegerField(unique=True, verbose_name='studentId')
    userType = models.CharField(max_length = 10, choices = userType, verbose_name = 'userType') 

    

class Application(models.Model):
    studentId = models.ForeignKey(registration, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True, verbose_name = 'dateTime')
    proponents = models.CharField(max_length = 50, unique = True, verbose_name='proponents')
    thesisTitle = models.TextField(verbose_name='title')

def __str__(self):
        return self.proponents

class status(models.Model):
    proponents = models.OneToOneField(Application, on_delete = models.CASCADE)
    dit = models.BooleanField(default=False, verbose_name='DIT')
    oaa = models.BooleanField(default=False, verbose_name='OAA')
    ocl = models.BooleanField(default=False, verbose_name='OCL')
    ore = models.BooleanField(default=False, verbose_name='ORE')
    adviser = models.BooleanField(default=False, verbose_name='ADVISER')
    fic = models.BooleanField(default=False, verbose_name='FIC')


