# Generated by Django 4.2.6 on 2023-11-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Secteur',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='Varieté',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
