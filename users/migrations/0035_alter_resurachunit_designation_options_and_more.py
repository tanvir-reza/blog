# Generated by Django 4.2 on 2023-11-26 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_resurachunit_designation_alter_people_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resurachunit_designation',
            options={'verbose_name': 'Research Unit Designation', 'verbose_name_plural': 'Research Unit Designations'},
        ),
        migrations.RemoveField(
            model_name='resurachunit_designation',
            name='dsgOrder',
        ),
        migrations.RemoveField(
            model_name='resurachunit_designation',
            name='slug',
        ),
    ]
