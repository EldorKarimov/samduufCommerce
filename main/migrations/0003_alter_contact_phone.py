# Generated by Django 4.2.11 on 2024-06-11 06:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_about_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=13, null=True, validators=[django.core.validators.RegexValidator('^[\\+]?[(]?[0-9]{3}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{4,6}$')], verbose_name='phone'),
        ),
    ]
