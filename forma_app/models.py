from django.db import models

# Create your models here.


class Job(models.Model):
    jobName = models.CharField(max_length=200,blank=True,null=True)
    education = models.CharField(max_length=100,blank=True,null=True)
    workExperience = models.CharField(max_length=100,blank=True,null=True,default="Белгиланмаган")
    personalSkills = models.CharField(max_length=150,blank=True,null=True,default="Белгиланмаган")
    languages = models.CharField(max_length=100,blank=True,null=True,default="Белгиланмаган")
    Place = models.CharField(max_length=200,blank=True,null=True,default="Белгиланмаган")
    jobText = models.TextField()
    JobDate = models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.jobName
    class Meta:
        ordering = ['JobDate']

class Interview(models.Model):
    interviewJob = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        blank=True,null=True
    )
    interviewDay = models.CharField(max_length=50)
    InterviewTime = models.PositiveSmallIntegerField()

class UserForm_uz(models.Model):
    rasm = models.ImageField(upload_to='media/rasmlar',null=True,blank=True)
    jobName = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    lastName = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200,blank=True,null=True)
    birthData = models.DateField()
    nation = models.CharField(max_length=50,blank=True,null=True)
    birthPlace = models.CharField(max_length=250)
    marriage_status = models.CharField(max_length=20)
    children = models.CharField(max_length=20)
    militaryResp = models.CharField(max_length=150)
    additionalCourses = models.CharField(max_length=300,blank=True,null=True)
    language_uzbek = models.CharField(max_length=150)
    language_russian = models.CharField(max_length=150)
    language_english = models.CharField(max_length=150,blank=True,null=True)
    language_boshqa = models.CharField(max_length=50, blank=True,null=True)
    computer_literacy = models.CharField(max_length=15)
    functional_resp = models.CharField(max_length=250,blank=True,null=True)
    work_experience = models.CharField(max_length=200,blank=True,null=True)
    yutuqlar = models.CharField(max_length=200,blank=True,null=True)
    leaving_work_reason = models.CharField(max_length=200,blank=True,null=True)
    main_skills = models.CharField(max_length=300,blank=True,null=True)
    personalSkills = models.CharField(max_length=50,blank=True,null=True)
    readinessWork = models.CharField(max_length=50,blank=True,null=True)
    hobby = models.CharField(max_length=150,blank=True,null=True)
    hobby_boshqa = models.CharField(max_length=200,blank=True,null=True)
    expected_salary = models.CharField(max_length=100,blank=True,null=True)
    reasontoWork = models.CharField(max_length=300,blank=True,null=True)
    relatives_company = models.CharField(max_length=300)
    criminal_history = models.CharField(max_length=250)
    homeNumber = models.CharField(max_length=15,blank=True,null=True)
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField(blank=True,null=True)
    additional_info = models.CharField(max_length=300,blank=True,null=True)
    approve_info = models.CharField(max_length=20)
    agreement = models.CharField(max_length=20)

    passport_file = models.FileField(upload_to='media/fayllar')
    diplom_file = models.FileField(upload_to='media/fayllar')
    trudovoyKnishka = models.FileField(upload_to='media/fayllar',blank=True,null=True)
    fullName = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName+ " " +self.lastName
    class Meta:
        ordering = ['time']

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

    def __str__(self):
        return self.form.firstName+" "+self.name

class Experience_uz(models.Model):
    form = models.ForeignKey(
        UserForm_uz,
        on_delete=models.CASCADE,
        blank = True, null = True
    )
    startWorkDate = models.DateField(blank=True,null=True)
    endWorkDate = models.DateField(blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    lavozim = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.form.firstName+" ish joyi: "+self.name

class Recommendation_uz(models.Model):
    form = models.ForeignKey(
        UserForm_uz,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    fullName = models.CharField(max_length=150,blank=True,null=True)
    workPlace = models.CharField(max_length=150,blank=True,null=True)
    phoneAndEmail = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return "Тавсиянома: "+self.form.firstName + " " + self.form.lastName + "га "+" "+self.fullName+"дан"

class OtherDocuments(models.Model):
    form = models.ForeignKey(
        UserForm_uz,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    file = models.FileField(upload_to='media/fayllar',null=True,blank=True)
    comment = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.form.firstName + " "+self.comment

