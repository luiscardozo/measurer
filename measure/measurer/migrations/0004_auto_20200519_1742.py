# Generated by Django 3.0.6 on 2020-05-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurer', '0003_auto_20200519_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expected',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]