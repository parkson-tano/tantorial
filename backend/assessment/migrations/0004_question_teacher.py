# Generated by Django 4.1.1 on 2022-10-01 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_first_name_alter_user_last_name'),
        ('assessment', '0003_assessmenttype_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.teacherprofile'),
        ),
    ]
