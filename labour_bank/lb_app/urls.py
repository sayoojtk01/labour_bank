from django.urls import path
from lb_app import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('service/', views.service),
    path('blog/', views.blog),
    path('employer/', views.employer),
    path('admin/', views.admin),
    path('contact/', views.contact),
    path('team/', views.team),
    path('service/', views.service),
    path('login/', views.login),
    path('logout/', views.logout),
    path('userregister/', views.register1),
    # path('message/',views.message),
    path('show/',views.usershow),
    path('useredit_user/',views.useredit_user),
    path('job/',views.job),
    path('add_job/',views.addjob),
    path('apply_job/',views.applyjob),
    path('emp_jobdelete/',views.emp_jobdelete),
    path('emp_profile/',views.emp_profile),
    # path('myjob/',views.myjob),
    











    # ---------ADMIN-------- #

    path('admin_index/', views.admin_index),
    path('admin_login/',views.admin_login),
    path('admin_register/',views.admin_register),
    path('employer_basictable/',views.employer_basictable),
    # path('admin_formcomponent/',views.admin_formcomponent),
    path('admin_logout/',views.admin_logout),
    path('employerupdate/',views.employerupdate),
    path('employerdelete/',views.employerdelete),
    path('message_tab/',views.message_tab),
    path('msg_delete/',views.msg_delete),
    path('job_view/',views.jobview),
    path('jobdelete/',views.job_delete),
    path('view_applicants/',views.view_applicants2),
    path('applicationdelete/',views.applicationdelete),

   
]