# Generated by Django 4.2.4 on 2023-08-31 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherassessment',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
