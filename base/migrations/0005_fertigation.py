# Generated by Django 4.2.6 on 2023-11-11 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_rename_description_task_parcelle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fertigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('date', models.CharField(blank=True, max_length=50)),
                ('ammonitrate', models.IntegerField(blank=True)),
                ('map', models.IntegerField(blank=True)),
                ('sulfate', models.IntegerField(blank=True)),
                ('calcium', models.IntegerField(blank=True)),
                ('case1', models.IntegerField(blank=True)),
                ('case2', models.IntegerField(blank=True)),
                ('organique', models.IntegerField(blank=True)),
                ('qté_eau', models.IntegerField(blank=True)),
                ('dure_irr', models.CharField(blank=True, max_length=50)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]