# Generated by Django 3.1.4 on 2021-01-10 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_department_sname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='sname',
            field=models.SlugField(unique=True),
        ),
    ]
