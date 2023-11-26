# Generated by Django 4.2 on 2023-11-26 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_rename_abstract_publications_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResurachUnit_Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250, unique=True)),
                ('dsgOrder', models.CharField(default='', max_length=3, unique=True)),
                ('slug', models.SlugField(default='', unique=True)),
            ],
            options={
                'verbose_name': 'Research Unit Designation',
                'verbose_name_plural': 'Research Unit Designations',
                'ordering': ['-dsgOrder'],
            },
        ),
        migrations.AlterField(
            model_name='people',
            name='category',
            field=models.CharField(choices=[('Founder & Research Director', 'Founder & Research Director'), ('Advisor', 'Advisor'), ('Head Of The Department', 'Head Of The Department'), ('Lead Researcher', 'Lead Researcher'), ('Researcher', 'Researcher'), ('Research Assistants', 'Research Assistants'), ('Research Intern', 'Research Intern'), ('Alumni', 'Alumni')], default='research_student', max_length=100),
        ),
        migrations.AddField(
            model_name='people',
            name='RU_Designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.resurachunit_designation', verbose_name='Research Unit Designation'),
        ),
    ]
