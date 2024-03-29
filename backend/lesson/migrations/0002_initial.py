# Generated by Django 4.1.5 on 2023-08-29 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subsystem', '0001_initial'),
        ('lesson', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='progression',
            name='class_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subsystem.classroom'),
        ),
        migrations.AddField(
            model_name='progression',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lesson',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.chapter'),
        ),
        migrations.AddField(
            model_name='competence',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.lesson'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='progression',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.progression'),
        ),
    ]
