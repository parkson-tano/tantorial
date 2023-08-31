# Generated by Django 4.1.5 on 2023-08-29 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subsystem', '0001_initial'),
        ('profiles', '0001_initial'),
        ('assessment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherassessment',
            name='assessment_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subsystem.classroom'),
        ),
        migrations.AddField(
            model_name='teacherassessment',
            name='assessment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.assessmenttype'),
        ),
        migrations.AddField(
            model_name='teacherassessment',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lesson.chapter'),
        ),
        migrations.AddField(
            model_name='teacherassessment',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lesson.lesson'),
        ),
        migrations.AddField(
            model_name='teacherassessment',
            name='taken_by',
            field=models.ManyToManyField(blank=True, related_name='taken_by', to='profiles.studentprofile'),
        ),
        migrations.AddField(
            model_name='teacherassessment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studentmark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studentmark',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.teacherassessment'),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.assessmentquestion'),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assessmenttarget',
            name='assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.teacherassessment'),
        ),
        migrations.AddField(
            model_name='assessmenttarget',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subsystem.classroom'),
        ),
        migrations.AddField(
            model_name='assessmenttarget',
            name='target',
            field=models.ManyToManyField(blank=True, related_name='target', to='profiles.studentprofile'),
        ),
        migrations.AddField(
            model_name='assessmentquestion',
            name='answered_by',
            field=models.ManyToManyField(blank=True, related_name='answered_by', to='profiles.studentprofile'),
        ),
        migrations.AddField(
            model_name='assessmentquestion',
            name='assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.teacherassessment'),
        ),
    ]