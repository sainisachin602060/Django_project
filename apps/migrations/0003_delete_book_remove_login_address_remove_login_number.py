# Generated by Django 4.1.3 on 2022-11-18 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.RemoveField(
            model_name='login',
            name='address',
        ),
        migrations.RemoveField(
            model_name='login',
            name='number',
        ),
    ]
