# Generated by Django 4.1.1 on 2022-09-29 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_parentprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'female')], max_length=10, null=True),
        ),
    ]