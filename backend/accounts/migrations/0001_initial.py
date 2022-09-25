# Generated by Django 4.1.1 on 2022-09-25 07:36

import accounts.utils
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('subsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=24)),
                ('profile_pic', models.ImageField(default='images/defaults/defaultuserprofile.svg', upload_to=accounts.utils.user_profile_path)),
                ('account_type', models.CharField(blank=True, choices=[('student', 'student'), ('parent', 'parent'), ('teacher', 'teacher'), ('school', 'school')], max_length=32, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=56)),
                ('profile_pic', models.ImageField(default='images/defaults/defaultuserprofile.svg', upload_to='schoolprofile/')),
                ('motto', models.CharField(blank=True, max_length=256, null=True)),
                ('code', models.CharField(max_length=16)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('school_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.schoolprofile')),
                ('subject', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='subsystem', chained_model_field='subsystem', null=True, on_delete=django.db.models.deletion.CASCADE, to='subsystem.subject')),
                ('subsystem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subsystem.subsystem')),
                ('teacher_class', smart_selects.db_fields.ChainedManyToManyField(chained_field='subsystem', chained_model_field='subsystem', to='subsystem.classroom')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_parent', to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.schoolprofile')),
                ('student_class', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='subsystem', chained_model_field='subsystem', null=True, on_delete=django.db.models.deletion.CASCADE, to='subsystem.classroom')),
                ('subsystem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subsystem.subsystem')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
