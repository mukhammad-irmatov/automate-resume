from django.db import models

# Create your models here.
language_choices = [('1', 'Билмайман'),
                    ('2', 'Ёмон'),
                    ('3', 'Лугат ёрдамида'),
                    ('4', 'Ўртача'),
                    ('5', 'Яхши'),
                    ('6', 'Жуда яхши'), ]
approve_choices = [('Yes', 'Ха'),
                    ('No', 'Йўк')]
agreement_choices = [('Yes', 'Ха'),
                    ('No', 'Йўк')]
class UserForm_uz(models.Model):
    # rasm = models.ImageField(upload_to='media/rasmlar',null=True,blank=True)
    lastName = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200)
    birthData = models.DateField()
    nation = models.CharField(max_length=50)
    birthPlace = models.CharField(max_length=250)
    marriage_status = models.CharField(max_length=20)
    children = models.CharField(max_length=20)
    militaryResp = models.CharField(max_length=150)
    language_uzbek = models.CharField(choices=language_choices,max_length=150)
    language_russian = models.CharField(choices=language_choices,max_length=150)
    language_english = models.CharField(choices=language_choices,max_length=150)
    language_boshqa = models.CharField(max_length=50, blank=True,null=True)
    computer_literacy = models.CharField(max_length=15)
    functional_resp = models.CharField(max_length=250)
    work_experience = models.CharField(max_length=200)
    yutuqlar = models.CharField(max_length=200)
    leaving_work_reason = models.CharField(max_length=200)
    main_skills = models.CharField(max_length=300)
    expected_salary = models.CharField(max_length=100)
    reasontoWork = models.CharField(max_length=300)
    relatives_company = models.CharField(max_length=300)
    criminal_history = models.CharField(max_length=250)
    homeNumber = models.CharField(max_length=15)
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()
    additional_info = models.CharField(max_length=300)
    approve_info = models.CharField(choices=approve_choices,max_length=20)
    agreement = models.CharField(choices=agreement_choices,max_length=20)

    # passport_file = models.FileField(upload_to='media/fayllar')
    # diplom_file = models.FileField(upload_to='media/fayllar')
    # trudovoyKnishka = models.FileField(upload_to='media/fayllar')
    fullName = models.CharField(max_length=100)

    def __str__(self):
        return self.fullName

class Education_uz(models.Model):
    form = models.ForeignKey(
        UserForm_uz,
        on_delete=models.CASCADE,
        blank=True,null=True
    )
    startingDate = models.DateField()
    endingDate = models.DateField()
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=50)
    speciality = models.CharField(max_length=150)
    diplomSeriya = models.CharField(max_length=50)


class Experience_uz(models.Model):
    form = models.ForeignKey(
        UserForm_uz,
        on_delete=models.CASCADE,
    )
    startWorkDate = models.DateField()
    endWorkDate = models.DateField()
    name = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Recommendation_uz(models.Model):
    form = models.ForeignKey(
        UserForm_uz,
        on_delete=models.CASCADE,
    )
    fullName = models.CharField(max_length=150)
    workPlace = models.CharField(max_length=150)
    phoneAndEmail = models.CharField(max_length=100)

class OtherDocuments(models.Model):
    form = models.ForeignKey(
        UserForm_uz,
        on_delete=models.CASCADE,
    )
    file = models.FileField(upload_to='media/fayllar',null=True,blank=True)
    comment = models.CharField(max_length=100)


