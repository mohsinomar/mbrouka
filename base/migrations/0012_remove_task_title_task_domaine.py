# Generated by Django 4.2.6 on 2023-11-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_remove_fertigation_name_remove_fertile_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
        migrations.AddField(
            model_name='task',
            name='domaine',
            field=models.CharField(max_length=50, null=True),
        ),
    ]