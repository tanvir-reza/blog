# Generated by Django 4.2 on 2023-05-22 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_blog_facebook_blog_linkedin_blog_opening_hours_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='opening_hours',
            field=models.TextField(blank=True, null=True),
        ),
    ]