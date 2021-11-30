# Generated by Django 3.2.9 on 2021-11-29 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserForm_uz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(blank=True, null=True, upload_to='media/rasmlar')),
                ('lastName', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=200)),
                ('middleName', models.CharField(blank=True, max_length=200, null=True)),
                ('birthData', models.DateField()),
                ('nation', models.CharField(blank=True, max_length=50, null=True)),
                ('birthPlace', models.CharField(max_length=250)),
                ('marriage_status', models.CharField(max_length=20)),
                ('children', models.CharField(max_length=20)),
                ('militaryResp', models.CharField(max_length=150)),
                ('additionalCourses', models.CharField(blank=True, max_length=300, null=True)),
                ('language_uzbek', models.CharField(max_length=150)),
                ('language_russian', models.CharField(max_length=150)),
                ('language_english', models.CharField(blank=True, max_length=150, null=True)),
                ('language_boshqa', models.CharField(blank=True, max_length=50, null=True)),
                ('computer_literacy', models.CharField(max_length=15)),
                ('functional_resp', models.CharField(blank=True, max_length=250, null=True)),
                ('work_experience', models.CharField(blank=True, max_length=200, null=True)),
                ('yutuqlar', models.CharField(blank=True, max_length=200, null=True)),
                ('leaving_work_reason', models.CharField(blank=True, max_length=200, null=True)),
                ('main_skills', models.CharField(blank=True, max_length=300, null=True)),
                ('personalSkills', models.CharField(blank=True, max_length=150, null=True)),
                ('readinessWork', models.CharField(blank=True, max_length=150, null=True)),
                ('hobby', models.CharField(blank=True, max_length=150, null=True)),
                ('hobby_boshqa', models.CharField(blank=True, max_length=200, null=True)),
                ('expected_salary', models.CharField(blank=True, max_length=100, null=True)),
                ('reasontoWork', models.CharField(blank=True, max_length=300, null=True)),
                ('relatives_company', models.CharField(max_length=300)),
                ('criminal_history', models.CharField(max_length=250)),
                ('homeNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('additional_info', models.CharField(blank=True, max_length=300, null=True)),
                ('approve_info', models.CharField(max_length=20)),
                ('agreement', models.CharField(max_length=20)),
                ('passport_file', models.FileField(upload_to='media/fayllar')),
                ('diplom_file', models.FileField(upload_to='media/fayllar')),
                ('trudovoyKnishka', models.FileField(blank=True, null=True, upload_to='media/fayllar')),
                ('fullName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation_uz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=150, null=True)),
                ('workPlace', models.CharField(blank=True, max_length=150, null=True)),
                ('phoneAndEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forma_app.userform_uz')),
            ],
        ),
        migrations.CreateModel(
            name='OtherDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='media/fayllar')),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forma_app.userform_uz')),
            ],
        ),
        migrations.CreateModel(
            name='Experience_uz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startWorkDate', models.DateField(blank=True, null=True)),
                ('endWorkDate', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('lavozim', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forma_app.userform_uz')),
            ],
        ),
        migrations.CreateModel(
            name='Education_uz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startingDate', models.DateField()),
                ('endingDate', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=50)),
                ('speciality', models.CharField(max_length=150)),
                ('diplomSeriya', models.CharField(max_length=50)),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forma_app.userform_uz')),
            ],
        ),
    ]
