# Generated by Django 4.2.10 on 2024-03-27 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Expo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlineform',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Expo_app.company'),
        ),
    ]