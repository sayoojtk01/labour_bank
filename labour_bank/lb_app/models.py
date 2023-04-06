from django.db import models

# Create your models here.

class register_tb(models.Model):
	name=models.CharField(max_length=255)
	sname=models.CharField(max_length=225)
	cpassword = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	address=models.CharField(max_length=225)
	gender=models.CharField(max_length=225)
	dob = models.CharField(max_length=255)
	education = models.CharField(max_length=255)
	jobcat=models.CharField(max_length=225)
	email=models.CharField(max_length=225)
	
	# image1=models.ImageField(upload_to="register/")


class adminregister_tb(models.Model):
	username=models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	password = models.CharField(max_length=255)



class message_tb(models.Model):
	name=models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	sub = models.CharField(max_length=255)
	msg = models.CharField(max_length=255)


class usergister_tb1(models.Model):
	name=models.CharField(max_length=255)
	sname=models.CharField(max_length=225)
	cpassword = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	address=models.CharField(max_length=225)
	gender=models.CharField(max_length=225)
	dob = models.CharField(max_length=255)
	education = models.CharField(max_length=255)
	jobcat=models.CharField(max_length=225)
	email=models.CharField(max_length=225)
	image1=models.ImageField(upload_to="register/")





class job_tb(models.Model):
	comapy=models.CharField(max_length=255)
	jtype=models.CharField(max_length=255)
	salary = models.CharField(max_length=255)
	time = models.CharField(max_length=255)
	vaccancy = models.CharField(max_length=255)


class applyjob_tb(models.Model):
	name=models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	exp = models.CharField(max_length=255)
	message=models.CharField(max_length=225)
	cv=models.FileField(upload_to="cv/")





