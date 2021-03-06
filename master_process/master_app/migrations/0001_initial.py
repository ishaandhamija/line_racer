# Generated by Django 2.0.13 on 2020-04-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LapMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lap_number', models.IntegerField()),
                ('slope1', models.IntegerField()),
                ('constant1', models.IntegerField()),
                ('slope2', models.IntegerField()),
                ('constant2', models.IntegerField()),
                ('lap_start_time', models.CharField(max_length=255)),
                ('lap_end_time', models.CharField(max_length=255)),
                ('lap_completion_time', models.BigIntegerField(null=True)),
                ('process_id', models.CharField(max_length=255)),
            ],
        ),
    ]
