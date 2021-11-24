from django import forms
from .models import UserForm_uz,Education_uz,Experience_uz,Recommendation_uz,OtherDocuments
from django.forms import modelformset_factory

marriage_choices = [('Married', 'Уйланган'),
                    ('Single', 'Бўйдок')]
children_choices = [('Yes', 'Ха'),
                    ('No', 'Йўк')]
computer_choices = [('0', 'Эга эмас'),
                    ('1', 'Бошлангич'),
                    ('2', 'Ўртача'),
                    ('3', 'Жуда яхши'),
                    ('4', 'Мукаммал ўзлаштирган'), ]
class MyForm(forms.ModelForm):
    birthData = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                input_formats=('%d/%m/%Y',))
    marriage_status = forms.ChoiceField(choices=marriage_choices, widget=forms.RadioSelect)
    children = forms.ChoiceField(choices=children_choices, widget=forms.RadioSelect)
    computer_literacy = forms.ChoiceField(choices=computer_choices,widget=forms.RadioSelect)

    class Meta:
        model = UserForm_uz
        fields = '__all__'

class EducationForm(forms.ModelForm):
    startingDate  = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                input_formats=('%d/%m/%Y',))
    endingDate = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                input_formats=('%d/%m/%Y',))
    class Meta:
        model = Education_uz
        exclude = ['form']

class ExperienceForm(forms.ModelForm):
    startWorkDate = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                    input_formats=('%d/%m/%Y',))
    endWorkDate = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                  input_formats=('%d/%m/%Y',))
    class Meta:
        model = Experience_uz
        exclude = ['form']


class RecommendationForm(forms.ModelForm):

    class Meta:
        model = Recommendation_uz
        exclude = ['form']

class OtherDocumentsForm(forms.ModelForm):
    class Meta:
        model = OtherDocuments
        exclude = ['form']


EducationFormSet = modelformset_factory(
    Education_uz,fields=("startingDate","endingDate","name","degree","speciality","diplomSeriya"),extra=1
)