# Generated by Django 3.0.9 on 2020-08-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0011_auto_20200830_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='expert_skills',
            field=models.ManyToManyField(blank=True, related_name='expert_skills', to='course_app.SkillModel'),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='intermediate_skills',
            field=models.ManyToManyField(blank=True, related_name='intermediate_skills', to='course_app.SkillModel'),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='novice_skills',
            field=models.ManyToManyField(blank=True, related_name='novice_skills', to='course_app.SkillModel'),
        ),
    ]
