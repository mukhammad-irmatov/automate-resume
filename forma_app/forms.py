from django import forms
from .models import UserForm_uz,Education_uz,Experience_uz,Recommendation_uz,OtherDocuments,Job
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
language_choices = (('1', 'Билмайман'),
                    ('2', 'Ёмон'),
                    ('3', 'Лугат ёрдамида'),
                    ('4', 'Ўртача'),
                    ('5', 'Яхши'),
                    ('6', 'Жуда яхши'), )
personalSkills_choices = [('интизомли', 'интизомли'),
                    ('1', 'ижрочи'),
                    ('2', 'тиришқоқ'),
                    ('3', 'ақлли'),
                    ('4', 'меҳнаткаш'),
                    ('5', 'ҳалол'),
                    ('6', 'ташаббускор'),
                    ('7','ташкилотчилик қобилияти'),
                    ('8','жамоада изчил ишлаш қобилияти'),
                    ('9', 'компаниянинг манфаатларини ҳимоя қилиш қобилияти'), ]

readinessWork_choices = [('1', '5 кунлик иш ҳафтаси'),
                    ('2', 'Командировка оддий'),
                    ('3', 'Командировка (яшаш жойи ўзгариши)'),
                    ('4', 'Иш жойи бощқа ҳудудга ўзгариши'),
                    ('5', 'Иш жойи бощқа давлатга ўзгариши'), ]
hobby_choices = [('1', 'Китоблар'),
                    ('2', 'Музей'),
                    ('3', 'Кино'),
                    ('4', 'Саёхат'),
                    ('5', 'Театр'),
                    ('6', 'Спорт'),
                    ('7', 'Дўстлар давраси'), ]
approve_choices = [('Yes', 'Ха'),
                    ('No', 'Йўк')]
agreement_choices = [('Yes', 'Ха'),
                    ('No', 'Йўк')]
class MyForm(forms.ModelForm):
    rasm  =forms.ImageField(label='Расмингизни киритинг')
    jobName = forms.ModelChoiceField(label="Ваканцияни танланг",queryset=Job.objects.all())
    lastName = forms.CharField(label='1. Фамилия', widget=forms.TextInput(attrs={'placeholder': 'Фамилиянгизни киритинг'}))
    firstName = forms.CharField(label='2. Исм', widget=forms.TextInput(attrs={'placeholder': 'Исмингизни киритинг'}))
    middleName = forms.CharField(label='3. Шарифингиз', widget=forms.TextInput(attrs={'placeholder': 'Шарифингизни киритинг'}))
    birthData = forms.DateField(label='Тугилган кунингиз',widget=forms.DateInput(format='%d/%m/%Y',attrs={'placeholder': 'Тугилган кунингизни киритинг'}),
                                input_formats=('%d/%m/%Y',))
    nation = forms.CharField(label='5. Миллати', widget=forms.TextInput(attrs={'placeholder': 'Миллати'}))
    birthPlace = forms.CharField(label='6. Туғилган жойи', widget=forms.TextInput(attrs={'placeholder': 'Туғилган жойи'}))
    marriage_status = forms.ChoiceField(label='7. Оилавий ҳолати',choices=marriage_choices, widget=forms.RadioSelect())
    children = forms.ChoiceField(label='8. Фарзандлари',choices=children_choices, widget=forms.RadioSelect)
    militaryResp = forms.CharField(label='9. Ҳарбий хизматга мажбурлигингиз ва ҳарбий унвонингиз', widget=forms.TextInput(attrs={'placeholder': 'Ҳарбий хизматга мажбурлигингиз ва ҳарбий унвонингиз борми'}))
    additionalCourses = forms.CharField(label='11. Қўшимча маълумот, малака ошириш, курслар ва тренинглар', widget=forms.TextInput(attrs={'placeholder': 'Қўшимча маълумот, малака ошириш, курслар ва тренингларда қатнашганмисиз'}))
    language_uzbek = forms.ChoiceField(label='Ўзбекча',choices=language_choices)
    language_russian= forms.ChoiceField(label='Русча',choices=language_choices)
    language_english = forms.ChoiceField(label='Инглизча',choices=language_choices)
    language_boshqa = forms.CharField(label='Бошка тил', widget=forms.TextInput(attrs={'placeholder': 'Бошка тил'}))
    computer_literacy = forms.ChoiceField(label='13. ЭҲМ да ишлаш ва программаларнинг турлари бўйича билим ва кўникмалар',choices=computer_choices,widget=forms.RadioSelect)
    functional_resp = forms.CharField(label='Ишдаги функционал мажбуриятлар', widget=forms.TextInput(attrs={'placeholder': 'Ишдаги функционал мажбуриятлар'}))
    work_experience = forms.CharField(label='Иш тажрибаси', widget=forms.TextInput(attrs={'placeholder': 'Иш тажрибаси'}))
    yutuqlar = forms.CharField(label='Ишдаги ютуқлар', widget=forms.TextInput(attrs={'placeholder': 'Иш давомидаги ютуқларингиз'}))
    leaving_work_reason = forms.CharField(label='15. Нима сабабдан сиз охирги иш жойингизни тарк этдингиз (ёки қарор қилдингиз)', widget=forms.TextInput(attrs={'placeholder': 'Нима сабабдан сиз охирги иш жойингизни тарк этдингиз (ёки қарор қилдингиз)'}))
    main_skills = forms.CharField(label='16. Асосий кўникмалар', widget=forms.TextInput(attrs={'placeholder': 'Асосий кўникмалар'}))
    personalSkills = forms.MultipleChoiceField(label='17. Шахсий фазилатларингиз',choices=personalSkills_choices,widget=forms.CheckboxSelectMultiple())
    readinessWork= forms.MultipleChoiceField(label='18. Ишга тайёрлигингиз',choices=readinessWork_choices,widget=forms.CheckboxSelectMultiple())
    hobby = forms.MultipleChoiceField(label='19. Қизиқишлар (хобби)',choices=hobby_choices,widget=forms.CheckboxSelectMultiple())
    hobby_boshqa = forms.CharField(label='Бошқа қизиқишлар', widget=forms.TextInput(attrs={'placeholder': 'Бошқа қизиқишлар'}))
    expected_salary = forms.CharField(label='20. Қанча ойлик маошга мўлжал қилмоқдасиз (сум)', widget=forms.TextInput(attrs={'placeholder': 'Қанча ойлик маошга мўлжал қилмоқдасиз (сум)'}))
    reasontoWork = forms.CharField(label='21. Сизни компаниямизда ишлашга нималар ундайди', widget=forms.TextInput(attrs={'placeholder': 'Сизни компаниямизда ишлашга нималар ундайди'}))
    relatives_company = forms.CharField(label='22. Ушбу компанияда ишлайдиган Сизга тегишли қариндош ёки алоқадор кишилар борми', widget=forms.TextInput(attrs={'placeholder': 'Ушбу компанияда ишлайдиган Сизга тегишли қариндош ёки алоқадор кишилар борми'}))
    criminal_history= forms.CharField(label='23. Маъмурий ёки жиноий жавобгарликка тортилганмисиз?', widget=forms.TextInput(attrs={'placeholder': 'Маъмурий ёки жиноий жавобгарликка тортилганмисиз?'}))
    homeNumber = forms.CharField(label='уй телефон рақами', widget=forms.TextInput(attrs={'placeholder': 'уй телефон рақами'}))
    phoneNumber = forms.CharField(label='мобил алоқа', widget=forms.TextInput(attrs={'placeholder': 'мобил алоқа'}))
    email = forms.CharField(label='e-mail', widget=forms.TextInput(attrs={'placeholder': 'e-mail'}))
    additional_info = forms.CharField(label='26. Ўзингиз ҳақингизда яна нималарни қўшимча қила оласиз', widget=forms.TextInput(attrs={'placeholder': 'Ўзингиз ҳақингизда яна нималарни қўшимча қила оласиз'}))
    approve_info = forms.ChoiceField(label='27. Ушбу резюмеда кўрсатилган маълумотларни тасдиқлайсизми ',choices=approve_choices, widget=forms.RadioSelect())
    agreement = forms.ChoiceField(label='28. Шахсий маълумотларингизни қайта ишлашимизга (ўрганишимизга) розилик берасизми',choices=agreement_choices, widget=forms.RadioSelect())
    passport_file = forms.FileField(label='Шахсни тасдиқловчи ҳужжат (Номзоднинг паспорти)')
    diplom_file = forms.FileField(label='Бирор таълим муассасасини тугатганлиги ҳақидаги диплом/сертификатлар битта архив файлда ')
    trudovoyKnishka = forms.FileField(label='МеҲнат дафтарчаси')
    fullName = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'placeholder': 'Тўлиқ фамилия исм-шарифингизни киритинг'}))

    class Meta:
        model = UserForm_uz
        fields = '__all__'

class EducationForm(forms.ModelForm):
    startingDate  = forms.DateField(label='Қабул қилинган сана',widget=forms.DateInput(format='%d/%m/%Y',attrs={'placeholder': 'Қабул қилинган сана'}),
                                input_formats=['%d/%m/%Y',])
    endingDate = forms.DateField(label='Тугаш санаси',widget=forms.DateInput(format='%d/%m/%Y',attrs={'placeholder': 'Тугаш санаси'}),
                                input_formats=['%d/%m/%Y',])
    name = forms.CharField(label='Ўқув муассасасинин тўлиқ номи', widget=forms.TextInput(attrs={'placeholder': 'Ўқув муассасасинин тўлиқ номи'}))
    degree = forms.CharField(label='Даражаси', widget=forms.TextInput(attrs={'placeholder': 'Даражаси (касб-хунар коллежи/бакалавр/магистр/доктор)'}))
    speciality = forms.CharField(label='Мутахассислиги', widget=forms.TextInput(attrs={'placeholder': 'Мутахассислиги'}))
    diplomSeriya = forms.CharField(label='Серия ва диплом №', widget=forms.TextInput(attrs={'placeholder': 'Серия ва диплом №'}))
    class Meta:
        model = Education_uz
        exclude = ['form']

class ExperienceForm(forms.ModelForm):
    startWorkDate = forms.DateField(label='Қабул қилинган сана',widget=forms.DateInput(format='%d/%m/%Y',attrs={'placeholder': 'Қабул қилинган сана'}),
                                    input_formats=['%d/%m/%Y',])
    endWorkDate = forms.DateField(label='Ишдан бушатиш санаси',widget=forms.DateInput(format='%d/%m/%Y',attrs={'placeholder': 'Ишдан бушатиш санаси'}),
                                  input_formats=['%d/%m/%Y',])
    name = forms.CharField(label='Ташкилот (корхона) номи', widget=forms.TextInput(attrs={'placeholder': 'Ташкилот (корхона) номи'}))
    lavozim = forms.CharField(label='Қайси лавозимда', widget=forms.TextInput(attrs={'placeholder': 'Қайси лавозимда ишлагансиз'}))
    address = forms.CharField(label='Ташкилот манзили',widget=forms.TextInput(attrs={'placeholder': 'Ташкилот манзили'}))

    class Meta:
        model = Experience_uz
        exclude = ['form']


class RecommendationForm(forms.ModelForm):
    fullName = forms.CharField(label='Ф.И.Ш. (тўлиқ)', widget=forms.TextInput(attrs={'placeholder': 'Ф.И.Ш. (тўлиқ)'}))
    workPlace = forms.CharField(label='Иш жойи, лавозими', widget=forms.TextInput(attrs={'placeholder': 'Иш жойи, лавозими'}))
    phoneAndEmail = forms.CharField(label='Телефон рақами, е-mail', widget=forms.TextInput(attrs={'placeholder': 'Телефон рақами, е-mail'}))
    class Meta:
        model = Recommendation_uz
        exclude = ['form']

class OtherDocumentsForm(forms.ModelForm):
    # file = forms.FileField(label='Хужжат')
    # comment = forms.CharField(label='Хужжатга изох', widget=forms.TextInput(attrs={'placeholder': 'Хужжатга изох (кандай хужжат эканлиги ҳақида)'}))
    # file = forms.FileField(label='Хужжат')
    comment = forms.CharField(label='Хужжатга изох')
    class Meta:
        model = OtherDocuments
        exclude = ['form']

class JobForm(forms.ModelForm):
    jobName = forms.CharField(label='Ваканция номи')
    class Meta:
        model = Job
        fields = "__all__"
# firstName = forms.CharField(label='2. Исм', widget=forms.TextInput(attrs={'placeholder': 'Исмингизни киритинг'}))