from django.contrib import admin
from .models import VoteUser, Users

# Register your models here.
admin.site.register(VoteUser)
admin.site.register(Users)