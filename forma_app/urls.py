from django.urls import path
from .views import AddFormView,adminPanelView,allApplicants,\
    AddJobView,AllJobsView,InterviewFormView,AllInterview,\
    ApplicantDetailView,HomePageView,AboutPageView,\
    JobdetailView,JobUpdateView,JobDeleteView


urlpatterns = [
    path('form',AddFormView.as_view(),name="addForm"),
    path('',HomePageView.as_view(),name='homepage'),
    path('about',AboutPageView.as_view(),name='about'),
    path('manager',adminPanelView.as_view(),name='dashboard'),
    path('manager/applicants',allApplicants.as_view(),name='all_applicants'),
    path('manager/applicants/<int:pk>',ApplicantDetailView.as_view(),name="applicantDetail"),
    path('manager/jobs/addJob',AddJobView.as_view(),name="addjob"),
    path('manager/jobs',AllJobsView.as_view(),name="all_jobs"),
    path('manager/jobs/<int:pk>/',JobdetailView.as_view(),name='jobdetail'),
    path('manager/jobs/<int:pk>/update',JobUpdateView.as_view(),name='jobUpdate'),
    path('manager/jobs/<int:pk>/delete',JobDeleteView.as_view(),name='jobDelete'),
    path('manager/interview',InterviewFormView.as_view(),name='interview'),
    path('manager/interview/all',AllInterview.as_view(),name='allinterview')


]