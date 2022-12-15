# Generated by Django 4.1.1 on 2022-12-12 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batch_ID', models.CharField(max_length=65, primary_key=True, serialize=False, verbose_name='Batch_ID')),
                ('batch_Qty', models.IntegerField(default=0, verbose_name='Batch_qty')),
                ('batch_Date', models.DateField(verbose_name='Batch_Date')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=65, primary_key=True, serialize=False, verbose_name='product_id')),
                ('product_name', models.CharField(max_length=65, verbose_name='model_name')),
                ('model_name', models.CharField(max_length=65, verbose_name='model_name')),
                ('price', models.CharField(max_length=10, verbose_name='price')),
                ('warranty', models.IntegerField(verbose_name='warranty')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_id', models.CharField(max_length=65, verbose_name='batch_ID')),
                ('status', models.CharField(default='Available', max_length=65, verbose_name='Product Name')),
                ('batch_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.batch')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product'),
        ),
    ]