# Generated by Django 4.1.3 on 2022-11-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
            ],
        ),
    ]
