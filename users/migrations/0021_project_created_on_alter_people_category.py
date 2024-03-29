# Generated by Django 4.2 on 2023-05-07 16:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_people_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='people',
            name='category',
            field=models.CharField(choices=[('advisor', 'Advisor'), ('research_assistant', 'Research Assistants'), ('founder_&_research_directors', 'Founder & Research Director'), ('research_coordinator_&_lead_research_assistant', 'Research Coordinator & Lead Research Assistant'), ('research_student', 'Research Student'), ('alumni', 'Alumni')], default='research_student', max_length=100),
        ),
    ]
