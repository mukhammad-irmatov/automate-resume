from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView,ListView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from .models import UserForm_uz,Education_uz,Experience_uz,Recommendation_uz,OtherDocuments
from .forms import MyForm,EducationForm,ExperienceForm,RecommendationForm,OtherDocumentsForm
from django.forms import modelformset_factory


class adminPanelView(ListView):
    model = UserForm_uz
    template_name = 'dashboard.html'

class allApplicants(ListView):
    model = UserForm_uz
    template_name = 'all_applicants.html'


class AddFormView(View):
    form_class = MyForm
    template_name = 'formuz.html'
    success_url = reverse_lazy('dashboard')

    # Define method to handle GET request
    def get(self, *args, **kwargs):
        # Create an instance of the formset
        EducationFormSet = modelformset_factory(Education_uz, form=EducationForm, extra=1)
        education_formset = EducationFormSet(queryset=Education_uz.objects.none())
        my_form = MyForm(prefix="form")
        return self.render_to_response({'my_form': my_form,'education_formset':education_formset})


    # Define method to handle POST request
    def post(self,request, *args, **kwargs):
        EducationFormSet = modelformset_factory(Education_uz, form=EducationForm, extra=1)
        education_formset = EducationFormSet(data=self.request.POST)
        my_form = self.form_class(request.POST,request.FILES,prefix='form')
        #check if submitted forms are valid
        if all([my_form.is_valid(), education_formset.is_valid()]):
            form = my_form.save()
            education = education_formset.save(commit=False)
            education.form = form
            education.save()
            # education_formset.save()
            return redirect(reverse_lazy('dashboard'))
        else:
            return HttpResponse("ishlamottiyu", content_type='text/plain')

        return self.render_to_response({'my_form': my_form,'education_formset':education_formset})



# def myFormView(request):
#     EducationFormSet = modelformset_factory(Education_uz,form=EducationForm,can_delete= True)
#     # ExperienceFormSet = modelformset_factory(Experience_uz,form = ExperienceForm,extra=2)
#     if request.method == 'POST':
#         my_form = MyForm(request.POST, request.FILES, prefix='form')
#         eduFormSet = EducationFormSet(request.POST,request.FILES,prefix='education')
#         # exprFormSet = ExperienceFormSet(request.POST,request.FILES,prefix='experience')
#
#         if all([my_form.is_valid(),eduFormSet.is_valid()]):
#             form = my_form.save()
#             education = eduFormSet.save(commit=False)
#
#             for edu in education:
#                 edu.form = form
#                 edu.save()
#             # education.form = form
#             # education.save()
#             # experience = exprFormSet.save(commit=False)
#             # experience.form = form
#             # experience.save()
#             return redirect('dashboard')
#     else:
#         my_form = MyForm(prefix='form')
#         eduFormSet = EducationFormSet(prefix='education')
#         # exprFormSet = ExperienceFormSet(prefix='experience')
#     return render(request,'resume.html',{'my_form': my_form, 'eduFormSet': eduFormSet})



