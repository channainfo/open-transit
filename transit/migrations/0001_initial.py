# Generated by Django 3.0.7 on 2020-06-10 01:35

import django.contrib.postgres.indexes
from django.db import migrations, models
import modeltrans.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=60000)),
                ('about', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('i18n', modeltrans.fields.TranslationField(fields=('name', 'short_description', 'description', 'about'), required_languages=(), virtual_fields=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='company',
            index=django.contrib.postgres.indexes.GinIndex(fields=['i18n'], name='transit_com_i18n_2fc1e3_gin'),
        ),
    ]
