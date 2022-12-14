# Generated by Django 4.1.1 on 2022-09-27 17:05

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('subsystem', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='student_class',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='subsystem', chained_model_field='subsystem', null=True, on_delete=django.db.models.deletion.CASCADE, to='subsystem.classroom'),
        ),
        migrations.AddField(
            model_name='user',
            name='subsystem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subsystem.subsystem'),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(blank=True, choices=[('student', 'Student'), ('parent', 'Parent'), ('teacher', 'Teacher'), ('school', 'School')], max_length=32, null=True),
        ),
    ]
