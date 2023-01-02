from django.db import models

# Create your models here.


class VoteUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email', unique=True)
    telephone = models.CharField(max_length=30)
    choix = models.CharField(max_length=50)
    updated_at = models.DateTimeField('Last Updated')

    def __str__(self):
        return self.first_name + " " + self.last_name
