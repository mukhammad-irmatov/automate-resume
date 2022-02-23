from django import forms
from .models import UserForm_uz,Education_uz,Experience_uz,Job,Interview


computer_choices = [('Эга эмас', 'Эга эмас'),
                    ('Бошлангич', 'Бошлангич'),
                    ('Ўртача', 'Ўртача'),
                    ('Жуда яхши', 'Жуда яхши'),
                    ('Мукаммал ўзлаштирган', 'Мукаммал ўзлаштирган'), ]
language_choices = (('Билмайман', 'Билмайман'),
                    ('Ёмон', 'Ёмон'),
                    ('Лугат ёрдамида', 'Лугат ёрдамида'),
                    ('Ўртача', 'Ўртача'),
                    ('Яхши', 'Яхши'),
                    ('Жуда яхши', 'Жуда яхши'), )



approve_choices = [('Ха', 'Ха'),
                    ('Йўк', 'Йўк')]
agreement_choices = [('Ха', 'Ха'),
                    ('Йўк', 'Йўк')]

days_choices = [('1', 'Душанба'),
                    ('2', 'Сешанба'),
                    ('3', 'Чоршанба'),
                    ('4', 'Пайшанба'),
                    ('5', 'Жуъма'), ]
class MyForm(forms.ModelForm):
    rasm  =forms.ImageField(label='Расмингизни киритинг')
    jobName = forms.ModelChoiceField(label="Ваканцияни танланг",queryset=Job.objects.all())
    lastName = forms.CharField(label='1. Фамилия', widget=forms.TextInput(attrs={'placeholder': 'Фамилиянгизни киритинг'}))
    firstName = forms.CharField(label='2. Исм', widget=forms.TextInput(attrs={'placeholder': 'Исмингизни киритинг'}))
    middleName = forms.CharField(label='3. Шарифингиз',required=False, widget=forms.TextInput(attrs={'placeholder': 'Шарифингизни киритинг'}))
    birthData = forms.DateField(label='Тугилган кунингиз',widget=forms.DateInput(format='%d/%m/%Y',attrs={'placeholder': '15/01/1998'}),
                                input_formats=('%d/%m/%Y',))

    nation = forms.CharField(label='5. Миллати',required=False, widget=forms.TextInput(attrs={'placeholder': 'Миллати'}))
    birthPlace = forms.CharField(label='6. Туғилган жойи', widget=forms.TextInput(attrs={'placeholder': 'Туғилган жойи'}))

    additionalCourses = forms.CharField(label='11. Қўшимча маълумот, малака ошириш, курслар ва тренинглар',required=False, widget=forms.TextInput(attrs={'placeholder': 'Қўшимча маълумот, малака ошириш, курслар ва тренингларда қатнашганмисиз'}))
    language_uzbek = forms.ChoiceField(label='Ўзбекча',choices=language_choices)
    language_russian= forms.ChoiceField(label='Русча',choices=language_choices)
    language_english = forms.ChoiceField(label='Инглизча',required=False,choices=language_choices)
    language_boshqa = forms.CharField(label='Бошка тил', required=False,widget=forms.TextInput(attrs={'placeholder': 'Бошка тил'}))
    computer_literacy = forms.ChoiceField(label='',choices=computer_choices,widget=forms.RadioSelect)

    homeNumber = forms.CharField(label='уй телефон рақами',required=False, widget=forms.TextInput(attrs={'placeholder': 'уй телефон рақами'}))
    phoneNumber = forms.CharField(label='мобил алоқа', required=False,widget=forms.TextInput(attrs={'placeholder': 'мобил алоқа'}))
    email = forms.CharField(label='e-mail', required=False,widget=forms.TextInput(attrs={'placeholder': 'e-mail'}))


    class Meta:
        model = UserForm_uz
        # fields = '__all__'
        exclude = ['time','test_id']



class EducationForm(forms.ModelForm):
    startingDate  = forms.DateField(label='Қабул қилинган сана',widget=forms.DateInput(format='%d/%m/%Y',attrs={'placeholder': '20/01/2020'}),
                                input_formats=['%d/%m/%Y',])
    endingDate = forms.DateField(label='Тугаш санаси',widget=forms.DateInput(format='%d/%m/%Y',attrs={'placeholder': '20/01/2020'}),
                                input_formats=['%d/%m/%Y',])
    name = forms.CharField(label='Ўқув муассасасинин тўлиқ номи', widget=forms.TextInput(attrs={'placeholder': 'Ўқув муассасасинин тўлиқ номи'}))
    degree = forms.CharField(label='Даражаси', widget=forms.TextInput(attrs={'placeholder': 'Даражаси (касб-хунар коллежи/бакалавр/магистр/доктор)'}))
    speciality = forms.CharField(label='Мутахассислиги', widget=forms.TextInput(attrs={'placeholder': 'Мутахассислиги'}))
    diplomSeriya = forms.CharField(label='Серия ва диплом №', widget=forms.TextInput(attrs={'placeholder': 'Серия ва диплом №'}))
    class Meta:
        model = Education_uz
        exclude = ['form']

class ExperienceForm(forms.ModelForm):
    startWorkDate = forms.DateField(label='Қабул қилинган сана',required=False,widget=forms.DateInput(format='%d/%m/%Y',attrs={'placeholder': '20/01/2020'}),
                                    input_formats=['%d/%m/%Y',])
    endWorkDate = forms.DateField(label='Ишдан бушатиш санаси',required=False,widget=forms.DateInput(format='%d/%m/%Y',attrs={'placeholder': '20/01/2020'}),
                                  input_formats=['%d/%m/%Y',])
    name = forms.CharField(label='Ташкилот (корхона) номи', required=False,widget=forms.TextInput(attrs={'placeholder': 'Ташкилот (корхона) номи'}))
    lavozim = forms.CharField(label='Қайси лавозимда', required=False,widget=forms.TextInput(attrs={'placeholder': 'Қайси лавозимда ишлагансиз'}))
    address = forms.CharField(label='Ташкилот манзили',required=False,widget=forms.TextInput(attrs={'placeholder': 'Ташкилот манзили'}))

    class Meta:
        model = Experience_uz
        exclude = ['form']


class JobForm(forms.ModelForm):
    jobName = forms.CharField(label='Ваканция номи', widget=forms.TextInput(attrs={'placeholder': 'ваканция номи'}))
    education = forms.CharField(label='Маълумоти', widget=forms.TextInput(attrs={'placeholder': 'мисол учун: orta maxsus, oliy'}))
    workExperience = forms.CharField(label='Иш тажрибаси', widget=forms.TextInput(attrs={'placeholder': 'мисол учун: 3 yillik tajriba'}))
    personalSkills = forms.CharField(label='Шахсий сифатлари',required=False, widget=forms.TextInput(attrs={'placeholder': 'мисол учун: chet tillarida faol'}))
    languages = forms.CharField(label='Тиллар', required=False,widget=forms.TextInput(attrs={'placeholder': 'мисол учун: Xitoy tili - Сўзлашув, Рус тили - erkin, Узбек тили - erkin'}))
    Place = forms.CharField(label='Иш жойи', required=False,widget=forms.TextInput(attrs={'placeholder': 'мисол учун: Тошкент вилояти'}))
    jobText = forms.CharField(label="Иш ҳақида батафсилроқ маълумот беринг",widget=forms.Textarea)

    class Meta:
        model = Job
        fields = "__all__"
# firstName = forms.CharField(label='2. Исм', widget=forms.TextInput(attrs={'placeholder': 'Исмингизни киритинг'}))

class InterviewForm(forms.ModelForm):
    interviewJob = forms.ModelChoiceField(label="Ваканцияни танланг",queryset=Job.objects.all())
    interviewDay = forms.CharField(label="Интервю кунини белгиланг")
    InterviewTime = forms.IntegerField(label='Intervyu boshlanish vaqtini yozing',widget=forms.NumberInput)
    class Meta:
        model =Interview
        fields = "__all__"
