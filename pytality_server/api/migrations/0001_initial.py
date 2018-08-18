# Generated by Django 2.1 on 2018-08-18 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('wrong_code', models.TextField()),
                ('correct_code', models.TextField()),
                ('task_title', models.CharField(max_length=256)),
                ('time_to_solve', models.IntegerField(default=5, validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(30)])),
            ],
        ),
    ]