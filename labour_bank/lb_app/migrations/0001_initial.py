# Generated by Django 4.1.7 on 2023-03-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=225)),
                ('cpassword', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=225)),
                ('gender', models.CharField(max_length=225)),
                ('dob', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('jobcat', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
            ],
        ),
    ]
