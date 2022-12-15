# Generated by Django 4.1.1 on 2022-12-13 11:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customersignup',
            name='phone_number',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MaxLengthValidator(11), django.core.validators.MinLengthValidator(11)]),
        ),
        migrations.AlterField(
            model_name='dealersignup',
            name='gst',
            field=models.IntegerField(max_length=65, verbose_name='gst'),
        ),
    ]
