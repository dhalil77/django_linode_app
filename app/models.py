from django.db import models

# Create your models here.


class VoteUser(models.Model):
    # id = models.IntegerField(primary_key = True)
    id = models.AutoField(primary_key = True, unique=True)
    first_name = models.CharField(max_length=30 , unique=True )
    last_name = models.CharField(max_length=30, unique=True)
    # email = models.EmailField('User Email', unique=True)
    telephone = models.CharField(max_length=30, unique=True)
    choix = models.CharField(max_length=50)
    # updated_at = models.DateTimeField('Last Updated')
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
