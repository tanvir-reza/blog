# Generated by Django 4.2 on 2023-05-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]