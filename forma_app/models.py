from django.db import models
import random
def random_string():
    return str(random.randint(10000, 99999))

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
    test_id = models.CharField(default = random_string, max_length=5)

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
    additionalCourses = models.CharField(max_length=300,blank=True,null=True)
    language_uzbek = models.CharField(max_length=150)
    language_russian = models.CharField(max_length=150)
    language_english = models.CharField(max_length=150,blank=True,null=True)
    language_boshqa = models.CharField(max_length=50, blank=True,null=True)
    computer_literacy = models.CharField(max_length=15)
    homeNumber = models.CharField(max_length=15,blank=True,null=True)
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField(blank=True,null=True)
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
