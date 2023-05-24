# Generated by Django 4.2 on 2023-05-22 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_project_created_on_alter_people_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='category',
            field=models.CharField(choices=[('Advisor', 'Advisor'), ('Research Assistant', 'Research Assistant'), ('Founder & Research Director', 'Founder & Research Director'), ('Research Coordinator & Lead Research Assistant', 'Research Coordinator & Lead Research Assistant'), ('Research Student', 'Research Student'), ('Alumni', 'Alumni')], default='research_student', max_length=100),
        ),
    ]
