# Generated by Django 4.0.3 on 2022-03-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('precipitation', models.FloatField()),
                ('temperature', models.FloatField()),
                ('was_raining', models.BooleanField()),
            ],
        ),
    ]
