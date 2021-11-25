from django.urls import path
from .views import AddFormView,adminPanelView,allApplicants

urlpatterns = [
    path('',AddFormView.as_view(),name="addForm"),
    # path('resume',myFormView,name='myForm'),
    path('manager',adminPanelView.as_view(),name='dashboard'),
    path('manager/applicants',allApplicants.as_view(),name='all_applicants'),

]