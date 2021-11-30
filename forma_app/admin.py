from django.contrib import admin
from .models import UserForm_uz,Education_uz,Experience_uz,Recommendation_uz,OtherDocuments,Job

# Register your models here.
admin.site.register(UserForm_uz)
admin.site.register(Education_uz)
admin.site.register(Experience_uz)
admin.site.register(Recommendation_uz)
admin.site.register(OtherDocuments)
admin.site.register(Job)