# Generated by Django 4.1.1 on 2022-12-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Signup', '0004_alter_customersignup_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealersignup',
            name='gst',
            field=models.CharField(max_length=65, verbose_name='gst'),
        ),
    ]
