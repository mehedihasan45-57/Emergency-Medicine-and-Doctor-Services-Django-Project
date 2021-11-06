# Generated by Django 3.1.7 on 2021-04-10 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0012_medicine_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.category'),
        ),
    ]