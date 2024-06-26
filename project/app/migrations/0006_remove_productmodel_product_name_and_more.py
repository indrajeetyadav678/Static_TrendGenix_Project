# Generated by Django 4.2.13 on 2024-05-24 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_productmodel_remove_registrationmodel_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='Product_Name',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Prod_Detail',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Prod_Image1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Prod_Image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Prod_Image3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Prod_Image4',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Prod_MRP',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Prod_Name',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Prod_Offer',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Prod_Price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Serial_no',
            field=models.IntegerField(null=True),
        ),
    ]
