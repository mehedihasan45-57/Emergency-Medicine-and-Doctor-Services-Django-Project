# Generated by Django 3.1.7 on 2021-03-24 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prescribed_history', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescribedhistory',
            old_name='doctor_id',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='prescribedhistory',
            old_name='user_id',
            new_name='user',
        ),
    ]