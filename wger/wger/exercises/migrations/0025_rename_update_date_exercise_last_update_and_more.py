# Generated by Django 4.1.9 on 2023-07-27 08:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('exercises', '0024_license_information'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='update_date',
            new_name='last_update',
        ),
        migrations.RenameField(
            model_name='exercisebase',
            old_name='update_date',
            new_name='last_update',
        ),
        migrations.RenameField(
            model_name='historicalexercise',
            old_name='update_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='historicalexercisebase',
            old_name='update_date',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='exercisebase',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='historicalexercise',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='historicalexercisebase',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='exercise',
            name='created',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercisebase',
            name='created',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exerciseimage',
            name='created',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name='Date',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exerciseimage',
            name='last_update',
            field=models.DateTimeField(
                auto_now=True,
                verbose_name='Date',
            ),
        ),
        migrations.AddField(
            model_name='exercisevideo',
            name='created',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name='Date',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercisevideo',
            name='last_update',
            field=models.DateTimeField(
                auto_now=True,
                verbose_name='Date',
            ),
        ),
        migrations.AddField(
            model_name='historicalexercise',
            name='last_update',
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                editable=False,
                verbose_name='Date',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalexercisebase',
            name='last_update',
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                editable=False,
                verbose_name='Date',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalexerciseimage',
            name='created',
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                editable=False,
                verbose_name='Date',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalexerciseimage',
            name='last_update',
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                editable=False,
                verbose_name='Date',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalexercisevideo',
            name='created',
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                editable=False,
                verbose_name='Date',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalexercisevideo',
            name='last_update',
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                editable=False,
                verbose_name='Date',
            ),
            preserve_default=False,
        ),
    ]
