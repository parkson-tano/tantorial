# Generated by Django 4.1.1 on 2022-09-30 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=56),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=56),
        ),
    ]
