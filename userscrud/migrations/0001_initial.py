# Generated by Django 4.1.2 on 2022-10-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersCrud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('document', models.PositiveIntegerField(max_length=20)),
                ('age', models.IntegerField(max_length=3)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=250)),
                ('phone_number', models.PositiveIntegerField(max_length=15)),
                ('profession', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]