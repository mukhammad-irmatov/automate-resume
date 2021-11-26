from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView,ListView,CreateView
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


class AddFormView(TemplateView):
    template_name = 'formuz.html'

    # Define method to handle GET request
    def get(self, *args, **kwargs):
        # Create an instance of the formset
        EducationFormSet = modelformset_factory(Education_uz, form=EducationForm, extra=1)
        education_formset = EducationFormSet(queryset=Education_uz.objects.none(),prefix='education')
        my_form = MyForm(prefix="form")
        return self.render_to_response({'my_form':my_form,'education_formset':education_formset})


    # Define method to handle POST request
    def post(self, *args, **kwargs):
        EducationFormSet = modelformset_factory(Education_uz, form=EducationForm, extra=1)
        education_formset = EducationFormSet(data = self.request.POST,prefix='education')
        my_form = MyForm(self.request.POST,self.request.FILES,prefix='form')
        print(education_formset)
        print(my_form)

        if education_formset.is_valid() and my_form.is_valid():
            form = my_form.save()
            education = education_formset.save(commit=False)
            for eduForma in education:
                eduForma.form = form
                eduForma.save()
            # education.form = form
            # education.save()
            # my_form.save()
            return redirect(reverse_lazy('dashboard'))
        # else:
        #     return HttpResponse("baribir ishlamottiyu", content_type='text/plain')

        return self.render_to_response({'my_form':my_form,'education_formset':education_formset})



# def AddFormView(request):
#     EducationFormSet = modelformset_factory(Education_uz, form=EducationForm, extra=1)
#
#     if request.method == 'POST':
#         my_form = MyForm(request.POST, request.FILES, prefix='form')
#         education_formset = EducationFormSet(request.POST, request.FILES, prefix='education')
#         # experience_form = ExperienceForm(request.POST, request.FILES, prefix='experience')
#         if all([my_form.is_valid(), education_formset.is_valid()]):
#             print(request.POST)
#             print(request.FILES)
#             form = my_form.save()
#             education = education_formset.save(commit=False)
#             education.form = form
#             education.save()
#
#
#             return redirect('dashboard')
#     else:
#         my_form = MyForm(prefix='form')
#         EducationFormSet = modelformset_factory(Education_uz, form=EducationForm, extra=1)
#         education_formset = EducationFormSet(request.GET or None,queryset=Education_uz.objects.none())
#
#     return render(request, 'formuz.html', {'my_form': my_form, 'education_formset': education_formset})



