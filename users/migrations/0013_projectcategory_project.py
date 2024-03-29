# Generated by Django 4.2 on 2023-05-03 15:14

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_rename_name_people_fullname_people_banglaname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectType', models.CharField(blank=True, default='', max_length=20)),
            ],
            options={
                'verbose_name': 'Projcet Type',
                'verbose_name_plural': 'Projcet Types',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_Title', models.CharField(default='', max_length=200)),
                ('abstract', ckeditor.fields.RichTextField(blank=True, default='', null=True)),
                ('Github_Link', models.CharField(default='', max_length=200)),
                ('Funding_agency', models.CharField(default='', max_length=200)),
                ('Funding_period', models.CharField(default='', max_length=200)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1)),
                ('total_views', models.IntegerField(default=0)),
                ('Author', models.ManyToManyField(default='', to='users.people')),
                ('ProjectCategory', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.projectcategory', verbose_name='Projcet Type')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
            },
        ),
    ]
