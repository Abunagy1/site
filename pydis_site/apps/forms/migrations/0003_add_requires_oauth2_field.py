# Generated by Django 2.2.13 on 2020-06-20 03:53

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_default_questions_to_dict'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='needs_oauth',
            field=models.BooleanField(default=False, help_text='Collect OAuth2 data from users filling out the form'),
        ),
        migrations.AlterField(
            model_name='form',
            name='questions',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, editable=False, help_text='The questions on the form in JSON format'),
        ),
    ]
