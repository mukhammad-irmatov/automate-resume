[1mdiff --git a/db.sqlite3 b/db.sqlite3[m
[1mindex 69c0477..dd9e3a5 100644[m
Binary files a/db.sqlite3 and b/db.sqlite3 differ
[1mdiff --git a/forma_app/__pycache__/views.cpython-39.pyc b/forma_app/__pycache__/views.cpython-39.pyc[m
[1mindex 3e7ee33..eb6ffde 100644[m
Binary files a/forma_app/__pycache__/views.cpython-39.pyc and b/forma_app/__pycache__/views.cpython-39.pyc differ
[1mdiff --git a/forma_app/views.py b/forma_app/views.py[m
[1mindex 2eac117..59fb67f 100644[m
[1m--- a/forma_app/views.py[m
[1m+++ b/forma_app/views.py[m
[36m@@ -26,6 +26,8 @@[m [mclass AddFormView(TemplateView):[m
         # Create an instance of the formset[m
         EducationFormSet = modelformset_factory(Education_uz, form=EducationForm, extra=1)[m
         education_formset = EducationFormSet(queryset=Education_uz.objects.none())[m
[32m+[m[32m        ExperienceFormSet = modelformset_factory(Experience_uz,form = ExperienceForm,extra=1)[m
[32m+[m[32m        experience_formset =  ExperienceFormSet(queryset=Experience_uz.objects.none())[m
         my_form = MyForm(prefix="form")[m
         return self.render_to_response({'my_form':my_form,'education_formset':education_formset})[m
 [m
[36m@@ -34,9 +36,10 @@[m [mclass AddFormView(TemplateView):[m
     def post(self, *args, **kwargs):[m
         EducationFormSet = modelformset_factory(Education_uz, form=EducationForm, extra=1)[m
         education_formset = EducationFormSet(data = self.request.POST)[m
[32m+[m[32m        ExperienceFormSet = modelformset_factory(Experience_uz, form=ExperienceForm, extra=1)[m
[32m+[m[32m        experience_formset = ExperienceFormSet(data=self.request.POST)[m
         my_form = MyForm(self.request.POST,self.request.FILES,prefix='form')[m
[31m-        print(education_formset)[m
[31m-        print(my_form)[m
[32m+[m
 [m
         if education_formset.is_valid() and my_form.is_valid():[m
             form = my_form.save()[m
[36m@@ -44,9 +47,11 @@[m [mclass AddFormView(TemplateView):[m
             for eduForma in education:[m
                 eduForma.form = form[m
                 eduForma.save()[m
[31m-            # education.form = form[m
[31m-            # education.save()[m
[31m-            # my_form.save()[m
[32m+[m[32m            experience = experience_formset.save(commit=False)[m
[32m+[m[32m            for exForma in experience:[m
[32m+[m[32m                exForma.form = form[m
[32m+[m[32m                exForma.save()[m
[32m+[m
             return redirect(reverse_lazy('dashboard'))[m
         # else:[m
         #     return HttpResponse("baribir ishlamottiyu", content_type='text/plain')[m
