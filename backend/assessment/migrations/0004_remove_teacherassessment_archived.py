# Generated by Django 4.2.4 on 2023-09-01 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0003_teacherassessment_archived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherassessment',
            name='archived',
        ),
    ]
