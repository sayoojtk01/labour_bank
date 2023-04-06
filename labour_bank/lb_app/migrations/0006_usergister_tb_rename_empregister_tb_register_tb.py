# Generated by Django 4.1.7 on 2023-03-31 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb_app', '0005_rename_register_tb_empregister_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='usergister_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sname', models.CharField(max_length=225)),
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
        migrations.RenameModel(
            old_name='empregister_tb',
            new_name='register_tb',
        ),
    ]
