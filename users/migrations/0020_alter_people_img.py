# Generated by Django 4.2 on 2023-05-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_about_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='img',
            field=models.FileField(blank=True, upload_to='people/', verbose_name='Photo'),
        ),
    ]
