# Generated by Django 4.1.1 on 2022-10-02 06:40

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0008_remove_question_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherassessment',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=0, editable=False, populate_from=('title', 'assessment_type')),
            preserve_default=False,
        ),
    ]
