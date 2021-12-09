from django.urls import path
from .views import AddFormView,adminPanelView,allApplicants,\
    AddJobView,AllJobsView,InterviewFormView,ApplicantDetailView,HomePageView
from django.contrib.auth.mixins import LoginRequiredMixin

urlpatterns = [
    path('form',AddFormView.as_view(),name="addForm"),
    path('',HomePageView.as_view(),name='homepage'),
    path('manager',adminPanelView.as_view(),name='dashboard'),
    path('manager/applicants',allApplicants.as_view(),name='all_applicants'),
    path('manager/applicants/<int:pk>',ApplicantDetailView.as_view(),name="applicantDetail"),
    path('manager/jobs/addJob',AddJobView.as_view(),name="addjob"),
    path('manager/jobs',AllJobsView.as_view(),name="all_jobs"),
    path('manager/interview',InterviewFormView.as_view(),name='interview'),


]