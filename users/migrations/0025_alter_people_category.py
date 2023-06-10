# Generated by Django 4.2 on 2023-06-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_openpositoncategory_openpositon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='category',
            field=models.CharField(choices=[('Advisor', 'Advisor'), ('Research Associates', 'Research Associates'), ('Research Assistants', 'Research Assistants'), ('Founder & Research Director', 'Founder & Research Director'), ('Research Coordinator & Lead R.A', 'Research Coordinator & Lead R.A'), ('Research Intern Student', 'Research Intern Student'), ('Alumni', 'Alumni')], default='research_student', max_length=100),
        ),
    ]
