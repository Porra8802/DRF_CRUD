# Generated by Django 4.1.2 on 2022-10-29 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReadExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.IntegerField(max_length=100)),
                ('B', models.IntegerField(max_length=100)),
                ('C', models.IntegerField(max_length=100)),
                ('D', models.IntegerField(max_length=100)),
                ('E', models.IntegerField(max_length=100)),
            ],
        ),
    ]
