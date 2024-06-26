# Generated by Django 4.2.13 on 2024-05-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Task', models.TextField()),
                ('Date', models.DateField(auto_now=True)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
