# Generated by Django 4.2 on 2023-05-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_people_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1),
        ),
    ]
