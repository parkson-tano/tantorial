# Generated by Django 4.1.1 on 2022-10-02 07:52

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0016_alter_teacherassessment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherassessment',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('assessment_type__title',)),
        ),
    ]
