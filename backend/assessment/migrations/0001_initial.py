# Generated by Django 4.1.5 on 2023-08-29 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('answer_a', models.TextField(blank=True, null=True)),
                ('answer_b', models.TextField(blank=True, null=True)),
                ('answer_c', models.TextField(blank=True, null=True)),
                ('answer_d', models.TextField(blank=True, null=True)),
                ('correct_answer', models.CharField(blank=True, max_length=15, null=True)),
                ('seen_count', models.IntegerField(default=0)),
                ('answered_count', models.IntegerField(default=0)),
                ('explanation', models.TextField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteria', models.CharField(blank=True, max_length=256, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_answer', models.CharField(blank=True, max_length=15, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False)),
                ('passed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False)),
                ('passed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(blank=True, max_length=256, null=True)),
                ('title', models.CharField(max_length=256)),
                ('taken_count', models.IntegerField(default=0)),
                ('complete_count', models.IntegerField(default=0)),
                ('publish', models.BooleanField(default=False)),
                ('dateline', models.DateTimeField(blank=True, null=True)),
                ('objective', models.TextField(blank=True, null=True)),
                ('competence', models.TextField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
