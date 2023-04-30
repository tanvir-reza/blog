# Generated by Django 4.1.7 on 2023-04-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_delete_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=40, null=True)),
                ('designation', models.TextField(blank=True, max_length=100, null=True)),
                ('university', models.TextField(blank=True, max_length=300, null=True)),
                ('category', models.CharField(choices=[('advisor', 'Advisor'), ('research_assistant', 'Research Assistant'), ('research_student', 'Research Student')], default='research_student', max_length=30)),
                ('img', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'People',
            },
        ),
    ]