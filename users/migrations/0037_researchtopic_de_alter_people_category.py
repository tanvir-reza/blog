# Generated by Django 4.2 on 2023-11-27 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_alter_people_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchtopic',
            name='de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.resurachunit_designation', verbose_name='Research Unit Designation'),
        ),
        migrations.AlterField(
            model_name='people',
            name='category',
            field=models.CharField(choices=[('Founder & Research Director', 'Founder & Research Director'), ('Advisor', 'Advisor'), ('Head of the Department', 'Head of the Department'), ('Lead Researcher', 'Lead Researcher'), ('Research Coordinator & Lead R.A', 'Research Coordinator & Lead R.A'), ('Research Assistants', 'Research Assistants'), ('Research Intern', 'Research Intern'), ('Alumni', 'Alumni')], default='research_student', max_length=100),
        ),
    ]