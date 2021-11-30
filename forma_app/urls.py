from django.urls import path
from .views import AddFormView,adminPanelView,allApplicants,AddJobView,AllJobsView,smsView

urlpatterns = [
    path('',AddFormView.as_view(),name="addForm"),
    # path('resume',myFormView,name='myForm'),
    path('manager',adminPanelView.as_view(),name='dashboard'),
    path('manager/applicants',allApplicants.as_view(),name='all_applicants'),
    path('manager/jobs/addJob',AddJobView.as_view(),name="addjob"),
    path('manager/jobs',AllJobsView.as_view(),name="all_jobs"),
    path('sms/',smsView,name="broadcastsms"),

]