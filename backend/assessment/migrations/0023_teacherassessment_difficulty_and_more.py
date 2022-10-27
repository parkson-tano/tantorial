# Generated by Django 4.1.1 on 2022-10-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0022_studentquestion_graded'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherassessment',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], default=0, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacherassessment',
            name='evaluated_competences',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacherassessment',
            name='evaluated_lesson',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacherassessment',
            name='evaluated_topic',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacherassessment',
            name='number_of_questions',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacherassessment',
            name='required_score_to_pass',
            field=models.IntegerField(default=0, help_text='required score in %'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacherassessment',
            name='time',
            field=models.IntegerField(default=0, help_text='duration of the quiz in minutes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(blank=True, choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')], max_length=2, null=True),
        ),
    ]
