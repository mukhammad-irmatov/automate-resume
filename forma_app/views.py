from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView,ListView,CreateView
from .models import UserForm_uz,Education_uz,Experience_uz,Recommendation_uz,OtherDocuments,Job
from .forms import MyForm,EducationForm,ExperienceForm,RecommendationForm,OtherDocumentsForm,JobForm
from django.forms import modelformset_factory
from django.conf import settings
from twilio.rest import Client

def smsView(request):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message = client.messages.create(to='+998993451598', from_='+12347040890', body='Assalomu aleykum Hurmatli ish qidiruvchi')

    print(message.sid)

    return HttpResponse("Rahmat SMS muvaffaqiyatli yuborildi")

class adminPanelView(ListView):
    model = UserForm_uz
    template_name = 'dashboard.html'

class allApplicants(ListView):
    model = UserForm_uz
    template_name = 'all_applicants.html'
    context_object_name = 'allApplicants'
    ordering = ['time']

class AddJobView(CreateView):
    form_class = JobForm
    template_name = "add_job.html"
    success_url = reverse_lazy('all_jobs')

# class InterviewCreateView(CreateView):
#     form_class = JobForm
#     template_name = "add_job.html"
#     success_url = reverse_lazy('all_jobs')

class AllJobsView(ListView):
    model = Job
    template_name = 'allJobs.html'
    context_object_name = 'all_jobs_context'

class AddFormView(TemplateView):
    template_name = 'formuz.html'

    # Define method to handle GET request
    def get(self, *args, **kwargs):
        # Create an instance of the formset
        # education formset
        EducationFormSet = modelformset_factory(Education_uz, form=EducationForm, extra=1)
        education_formset = EducationFormSet(queryset=Education_uz.objects.none(),prefix='education')
        # experience formset
        ExperienceFormSet = modelformset_factory(Experience_uz,form=ExperienceForm,extra=1)
        experience_formset = ExperienceFormSet(queryset=Experience_uz.objects.none(),prefix="experience")
        # recommendation formset
        RecommendFormSet = modelformset_factory(Recommendation_uz,form=RecommendationForm,extra=1)
        recommend_formset = RecommendFormSet(queryset=Recommendation_uz.objects.none(),prefix='recommend')
        # OtherDocuments formset
        OtherDocsFormSet = modelformset_factory(OtherDocuments,form=OtherDocumentsForm,extra=1)
        otherdocs_formset = OtherDocsFormSet(queryset=OtherDocuments.objects.none(), prefix='otherdocs')

        my_form = MyForm(prefix="form")
        return self.render_to_response({'my_form':my_form,'education_formset':education_formset,'experience_formset':experience_formset,'recommend_formset':recommend_formset,'otherdocs_formset':otherdocs_formset})


    # Define method to handle POST request
    def post(self, *args, **kwargs):
        # education formset
        EducationFormSet = modelformset_factory(Education_uz, form=EducationForm, extra=1)
        education_formset = EducationFormSet(data = self.request.POST,prefix='education')
        # experience formset
        ExperienceFormSet = modelformset_factory(Experience_uz,form=ExperienceForm,extra=1)
        experience_formset = ExperienceFormSet(data=self.request.POST,prefix="experience")
        # recommendation formset
        RecommendFormSet = modelformset_factory(Recommendation_uz,form=RecommendationForm,extra=1)
        recommend_formset = RecommendFormSet(data=self.request.POST,prefix='recommend')
        # OtherDocuments formset
        OtherDocsFormSet = modelformset_factory(OtherDocuments,form=OtherDocumentsForm,extra=1)
        otherdocs_formset = OtherDocsFormSet(data=self.request.POST,prefix='otherdocs')

        my_form = MyForm(self.request.POST,self.request.FILES,prefix='form')
        print(education_formset)
        print(my_form)

        if education_formset.is_valid() and my_form.is_valid() and education_formset.is_valid() and recommend_formset.is_valid() and otherdocs_formset.is_valid():
            form = my_form.save()
            education = education_formset.save(commit=False)
            for eduForma in education:
                eduForma.form = form
                eduForma.save()

            experience = experience_formset.save(commit=False)
            for expForma in experience:
                expForma.form = form
                expForma.save()
            recommend = recommend_formset.save(commit=False)
            for recomForma in recommend:
                recomForma.form = form
                recomForma.save()
            otherdocument = otherdocs_formset.save(commit=False)
            for otherdocsForma in otherdocument:
                otherdocsForma.form = form
                otherdocsForma.save()

            return redirect(reverse_lazy('dashboard'))
        else:
            return HttpResponse(my_form.errors)

        return self.render_to_response({'my_form':my_form,'education_formset':education_formset,'experience_formset':experience_formset,'recommend_formset':recommend_formset,'otherdocs_formset':otherdocs_formset})




