# Generated by Django 4.2.6 on 2023-11-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_task_title_task_domaine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertile',
            name='destination',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
