# Generated by Django 3.1.4 on 2021-01-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_auto_20210111_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
