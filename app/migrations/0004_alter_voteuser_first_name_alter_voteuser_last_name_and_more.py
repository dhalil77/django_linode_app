# Generated by Django 4.1.4 on 2023-01-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_voteuser_email_alter_voteuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voteuser',
            name='first_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='voteuser',
            name='last_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='voteuser',
            name='telephone',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
