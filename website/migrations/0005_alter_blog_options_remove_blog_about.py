# Generated by Django 4.2 on 2023-06-10 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_blog_opening_hours'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Site Info', 'verbose_name_plural': 'Site Info'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='about',
        ),
    ]
