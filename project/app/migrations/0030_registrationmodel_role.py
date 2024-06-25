# Generated by Django 5.0.6 on 2024-06-25 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_invoicemodel_email_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='Role',
            field=models.CharField(choices=[('customer', 'customer'), ('admin', 'admin')], default='customer', max_length=20),
        ),
    ]
