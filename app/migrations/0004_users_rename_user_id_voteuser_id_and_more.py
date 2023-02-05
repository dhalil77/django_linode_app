# Generated by Django 4.1.4 on 2023-02-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_voteuser_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=30, unique=True)),
                ('last_name', models.CharField(max_length=30, unique=True)),
                ('telephone', models.CharField(max_length=30, unique=True)),
                ('choix', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='voteuser',
            old_name='User_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='voteuser',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='voteuser',
            name='status',
        ),
        migrations.RemoveField(
            model_name='voteuser',
            name='ville',
        ),
    ]
