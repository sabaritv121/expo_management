# Generated by Django 4.2.10 on 2024-03-28 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expo_app', '0005_booktickets_mobile_alter_booktickets_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='createexpo',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]