# Generated by Django 3.1.3 on 2020-11-11 15:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_auto_20201111_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'use correct charactors.')]),
        ),
    ]
