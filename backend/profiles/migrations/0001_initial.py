# Generated by Django 4.1.1 on 2023-07-26 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subsystem', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuardianProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=56, null=True)),
                ('last_name', models.CharField(blank=True, max_length=56, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('profile_picture', models.ImageField(default='images/defaults/defaultguardianprofile.svg', upload_to='guardianprofile/')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=56)),
                ('school_address', models.CharField(blank=True, max_length=256, null=True)),
                ('school_logo', models.ImageField(default='images/defaults/defaultschoollogo.svg', upload_to='schoolprofile/')),
                ('school_type', models.CharField(blank=True, max_length=56, null=True)),
                ('motto', models.CharField(blank=True, max_length=256, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subsystem.country')),
                ('cycle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subsystem.cycle')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subsystem.division')),
                ('locality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subsystem.locality')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subsystem.region')),
                ('school_language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subsystem.language')),
                ('sub_division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subsystem.subdivision')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=56, null=True)),
                ('last_name', models.CharField(blank=True, max_length=56, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=56, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('profile_picture', models.ImageField(default='images/defaults/defaultstudentprofile.svg', upload_to='studentprofile/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subsystem.language')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.schoolprofile')),
                ('student_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subsystem.classroom')),
                ('subsystem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subsystem.subsystem')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=56, null=True)),
                ('last_name', models.CharField(blank=True, max_length=56, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=56, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('profile_picture', models.ImageField(default='images/defaults/defaultteacherprofile.svg', upload_to='teacherprofile/')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.schoolprofile')),
                ('subsystem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subsystem.subsystem')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subsystem.subject')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.teacherprofile')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.studentprofile')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subsystem.subject')),
            ],
        ),
        migrations.CreateModel(
            name='StudentGuardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('guardian', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.guardianprofile')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.studentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ClassTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('class_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subsystem.classroom')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.teacherprofile')),
            ],
        ),
    ]