# Generated by Django 4.2.10 on 2024-03-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expo_app', '0003_onlineform_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlineform',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
