from django.db import models

# Create your models here.

class VoteUser(models.Model):
    # id = models.IntegerField(primary_key = True)
    id = models.AutoField(primary_key = True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30, unique=True)
    choix = models.CharField(max_length=50)
    ville = models.CharField(max_length=50, default=False)
    adresse = models.CharField(max_length=250, default=False)
    status = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name + " " + self.last_name


class User_rcsm(models.Model):
    # id = models.IntegerField(primary_key = True)
    user_id = models.AutoField(primary_key = True, unique=True)
    first_name = models.CharField(max_length=30 )
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30, unique=True)
    choix = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    adresse = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    # updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name + " " + self.last_name
