from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from .models import *
import os 
import datetime
import random
import string
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def index(request):
    mydata=job_tb.objects.all()
    return render(request,"index.html",{"data17":mydata})

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")

def blog(request):
    return render(request,"blog.html")

def employer(request):
    return render(request,"employer.html")

def admin(request):
    return render(request,"admin.html")

# def contact(request):
#     return render(request,"contact.html")

def team(request):
    return render(request,"team.html")

def service(request):
    return render(request,"services.html")

def login(request):
    if request.method=="POST":
        lemail=request.POST['email']
        lpassword=request.POST['psd']
        check=usergister_tb1.objects.filter(email=lemail,password=lpassword)
        if check:
            for x in check:
                request.session["id"]=x.id
                request.session["gname"]=x.name
                request.session["sname"]=x.sname
                # request.session["job"]=x.jobcat
                request.session["add"]=x.address
                # request.session["ed"]=x.education
                request.session["im"]=x.image1.url
            return HttpResponseRedirect('/')
        else:            
            return render(request,"login.html",{"err":"Unregistered please register"})
    else:
        return render(request,"login.html")


# def register(request):
#     if request.method=="POST":
#         fname=request.POST['fname']
#         lname=request.POST['lname']
#         password=request.POST['password']
#         cpassword=request.POST['cpassword']
#         address=request.POST['address']
#         gender=request.POST['gender']
#         dob=request.POST['dob']
#         education=request.POST['education']
#         jobcat=request.POST['jobcat']
#         email=request.POST['email']

#         check=usergister_tb1.objects.filter(email=email)

#         if password==cpassword:
#             if check:
#                 return render(request,"register.html",{"error":"email already registered"})
                
#             else:
#                 add=usergister_tb1(name=fname,sname=lname,password=password,cpassword=cpassword,address=address,gender=gender
#                                 ,dob=dob,education=education,jobcat=jobcat,email=email)
#                 add.save()
#                 return render(request,"login.html")
#         else:
#             return render(request,"register.html",{"error1":"passwords doesn't match"})
#     else:
#         return render(request,"register.html")



def register1(request):
    if request.method=="POST":
        fname=request.POST['firstname']
        lname=request.POST['secondname']
        password=request.POST['psd']
        cpassword=request.POST['cpsd']
        address=request.POST['address']
        # gender=request.POST['gender']
        # dob=request.POST['dob']
        # education=request.POST['education']
        # jobcat=request.POST['jobct']
        email=request.POST['email']
        img=request.FILES["imageusr"]

        check=usergister_tb1.objects.filter(email=email)
        check2=usergister_tb1.objects.filter(name=fname)

        if password==cpassword:
            if check2:
                return render(request,"newreg.html",{"error57":"Company name already exist"}) 
            elif check:
                return render(request,"newreg.html",{"error56":"Company details already registered"})
            
            else:
                add=usergister_tb1(name=fname,sname=lname,password=password,cpassword=cpassword,address=address,email=email,image1=img)
                add.save()
                return render(request,"login.html")
        else:
            return render(request,"newreg.html",{"error58":"passwords doesn't match"})
    else:
        return render(request,"newreg.html")






def logout(request):
    if request.session.has_key('id'):
        del request.session["id"]
        del request.session["gname"]
        return redirect("/login/")
    else:
        return redirect("/")
    

# def message(request):
#     if request.session.has_key('id'):
#         if request.method=="POST":
#             name=request.POST['name']
#             email=request.POST['email']
#             sub=request.POST['subject']
#             msg=request.POST['message']
#             add=message_tb(name=name,email=email,sub=sub,msg=msg)
#             add.save()
#             return HttpResponseRedirect("/contact/")
#         else:
#             return redirect("/contact/")
#     else:
#         return redirect('/login/',{"error234":"Please Login Or Register "})
   

def usershow(request):
    if request.session.has_key('id'):
        mydata=usergister_tb1.objects.all()
        return render(request,"/",{"data3":mydata})
    else:
        return HttpResponseRedirect('/login/')
    
    

def useredit_user(request):
    if request.session.has_key('id'):
        if request.method == "POST":
            fname=request.POST['firstname']
            lname=request.POST['secondname']
            password=request.POST['psd']
            cpassword=request.POST['cpsd']
            address=request.POST['address']
            # gender=request.POST['gender']
            # dob=request.POST['dob']
            # education=request.POST['education']
            # jobcat=request.POST['jobct']
            email=request.POST['email']
            # img=request.FILES["imageusr"]
            uid=request.GET['uid']
            checkbox=request.POST["imgup"]
            if checkbox == "yes":
                ad_image=request.FILES["image"]
                oldrec=usergister_tb1.objects.filter(id=uid)
                updrec=usergister_tb1.objects.get(id=uid)
                for x in oldrec:
                    imageurl=x.image1.url
                    pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imageurl
                    if os.path.exists(pathtoimage):
                        os.remove(pathtoimage)
                        print('Successfully deleted')
                updrec.image1=ad_image
                updrec.save()
                print("-----------------")

            add=usergister_tb1.objects.filter(id=uid).update(name=fname,sname=lname,address=address,
                                email=email,password=password,cpassword=cpassword)
            return render(request,"index.html",{"msg":"updated successfully please login again"})
        else:
            uid=request.GET['uuid']
            mydata=usergister_tb1.objects.filter(id=uid)
            return render(request,"useredit.html",{"data123":mydata})
    else:
        return HttpResponseRedirect('/login/')
    


def contact(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['message']
       
        subject = 'Contact Form'
        message = f'There is message from {name} email {email}. The message is {msg}. Thankyou.'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [settings.EMAIL_HOST_USER, ] 
        send_mail( subject, message, email_from, recipient_list ) 
       
        subject = ' thank for submitting Contact Form'
        message = f'Hi {name}, Thankyou for submitting form.'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email, ] 
        send_mail( subject, message, email_from, recipient_list ) 

        return render(request,"index.html")
    else:
        return render(request,"contact.html")


def job(request):
    mydata=job_tb.objects.all()
    return render(request,"job/job-list.html",{"data18":mydata})

def addjob(request):
    if request.method=="POST":
        company=request.POST['cmpy']
        jname=request.POST['jname']
        salary=request.POST['salary']
        time=request.POST['time']
        vaccancy=request.POST['vaccancy']
        
        add=job_tb(jtype=jname,salary=salary,time=time,vaccancy=vaccancy,comapy=company)
        add.save()
        return render(request,"job/job-add.html",{"msg15":"Add Job  successfully "})
    else:
        return render(request,"job/job-add.html",{"msg16":"Not Add Try Again"})   


def applyjob(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        exp=request.POST['experience']
        message=request.POST['message']
        cv=request.FILES['cv']
        add=applyjob_tb(name=name,email=email,exp=exp,message=message,cv=cv)
        add.save()
        return render(request,"job/job-apply.html",{"msg19":"Add Job  successfully "})
    else:
        return render(request,"job/job-apply.html")



def emp_jobdelete(request):
     uid=request.GET['uuid']
     mydata=job_tb.objects.filter(id=uid).delete()
     return HttpResponseRedirect("/")

# def userjob_view(request):
#     mydata=job_tb.objects.all()
#     return render(request,"admin/jobview.html",{"data18":mydata})
    

def emp_profile(request):
    if request.session.has_key('id'):
        
        mydata=usergister_tb1.objects.all()
        for x in mydata:
                request.session["id"]=x.id
                request.session["gname"]=x.name
                request.session["sname"]=x.sname
                # request.session["job"]=x.jobcat
                request.session["add"]=x.address
                # request.session["ed"]=x.education
                request.session["im"]=x.image1.url
        return render(request,"emp_profile.html",{"data3":mydata})
    else:
        return HttpResponseRedirect('/login/')
    








    








# ------------ADMIN------------ #


def admin_index(request):
    if request.session.has_key('id'):
        return render(request,"admin/index.html")
    else:
        return HttpResponseRedirect('/admin_login/')
    

def admin_login(request):
    if request.method=="POST":
        lemail=request.POST['Email']
        lpassword=request.POST['Password']
        check=adminregister_tb.objects.filter(email=lemail,password=lpassword)
        if check:
            for x in check:
                request.session["id"]=x.id
                request.session["name"]=x.username
            return render(request,"admin/index.html")
        else:            
            return render(request,"admin/registration.html",{"err123":"Unregistered please register"})
    else:
        return render(request,"admin/login.html")




def employer_basictable(request):
    if request.session.has_key('id'):
        mydata=usergister_tb1.objects.all()
        return render(request,"admin/basic_table.html",{"data34":mydata})
    else:
        return HttpResponseRedirect('/admin_login/')
    

def employerupdate(request):
    
    if request.method == "POST":
        afname=request.POST['fname']
        alname=request.POST['lname']
        # password=request.POST['password']
        # cpassword=request.POST['cpassword']
        aaddress=request.POST['address']
        # agender=request.POST['gender']
        # adob=request.POST['dob']
        # aeducation=request.POST['education']
        # ajobcat=request.POST['jobcat']
        aemail=request.POST['email']
        uid=request.GET['uid']
        add=usergister_tb1.objects.filter(id=uid).update(name=afname,sname=alname,address=aaddress
                                ,email=aemail)
        return HttpResponseRedirect("/employer_basictable/")
    else:
        uid=request.GET['uuid']
        mydata=usergister_tb1.objects.filter(id=uid)
        return render(request,"admin/employerupdate.html",{"data1":mydata})
    

def employerdelete(request):
     uid=request.GET['uuid']
     mydata=usergister_tb1.objects.filter(id=uid).delete()
     return HttpResponseRedirect("/employer_basictable/")


def admin_register(request):
    if request.method == "POST":
        adname=request.POST["Name"]
        ademail=request.POST["Email"]
        adphone=request.POST["Phone"]
        adpassword=request.POST["Password"]
        check=adminregister_tb.objects.filter(email=ademail)
        if check:
                return render(request,"admin/registration.html",{"error32":"email already registered"})
        else:
                add=adminregister_tb(username=adname,email=ademail,phone=adphone,password=adpassword)
                add.save()
                return render(request,"admin/registration.html",{"success":"Register Successfully please login"})
    else:
        return render(request,"admin/registration.html")
    

def admin_logout(request):
    if request.session.has_key('id'):
        del request.session["id"]
        del request.session["name"]
    return redirect('/admin_login/')



def message_tab(request):
    if request.session.has_key('id'):
        mydata=message_tb.objects.all()
        return render(request,"admin/msgtable.html",{"data1":mydata})
    else:
        return HttpResponseRedirect('/admin_login/')
    

def msg_delete(request):
     uid=request.GET['uuid']
     mydata=message_tb.objects.filter(id=uid).delete()
     return HttpResponseRedirect("/message_tab/")


def jobview(request):
    if request.session.has_key('id'):
        mydata=job_tb.objects.all()
        return render(request,"admin/jobview.html",{"data15":mydata})
    else:
        return HttpResponseRedirect('/admin_login/')
    
def job_delete(request):
     uid=request.GET['uuid']
     mydata=job_tb.objects.filter(id=uid).delete()
     return HttpResponseRedirect("/job_view/")


def view_applicants2(request):
    if request.session.has_key('id'):
        mydata=applyjob_tb.objects.all()
        return render(request,"admin/abc.html",{"data20":mydata})
    else:
        return HttpResponseRedirect('/admin_login/')

def applicationdelete(request):
     uid=request.GET['uuid']
     mydata=applyjob_tb.objects.filter(id=uid).delete()
     return HttpResponseRedirect("/view_applicants/")