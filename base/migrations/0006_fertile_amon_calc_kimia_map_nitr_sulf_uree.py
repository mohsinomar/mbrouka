# Generated by Django 4.2.6 on 2023-11-11 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_fertigation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fertile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('date', models.CharField(blank=True, max_length=50)),
                ('s_initial', models.IntegerField(blank=True)),
                ('entree', models.IntegerField(blank=True)),
                ('sortie', models.IntegerField(blank=True)),
                ('destination', models.IntegerField(blank=True)),
                ('s_restant', models.IntegerField(blank=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Amon',
            fields=[
                ('fertile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.fertile')),
            ],
            bases=('base.fertile',),
        ),
        migrations.CreateModel(
            name='Calc',
            fields=[
                ('fertile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.fertile')),
            ],
            bases=('base.fertile',),
        ),
        migrations.CreateModel(
            name='Kimia',
            fields=[
                ('fertile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.fertile')),
            ],
            bases=('base.fertile',),
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('fertile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.fertile')),
            ],
            bases=('base.fertile',),
        ),
        migrations.CreateModel(
            name='Nitr',
            fields=[
                ('fertile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.fertile')),
            ],
            bases=('base.fertile',),
        ),
        migrations.CreateModel(
            name='Sulf',
            fields=[
                ('fertile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.fertile')),
            ],
            bases=('base.fertile',),
        ),
        migrations.CreateModel(
            name='Uree',
            fields=[
                ('fertile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.fertile')),
            ],
            bases=('base.fertile',),
        ),
    ]