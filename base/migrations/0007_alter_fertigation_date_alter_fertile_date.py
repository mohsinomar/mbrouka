# Generated by Django 4.2.6 on 2023-11-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_fertile_amon_calc_kimia_map_nitr_sulf_uree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertigation',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='fertile',
            name='date',
            field=models.DateField(null=True),
        ),
    ]