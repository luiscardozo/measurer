# Generated by Django 3.0.6 on 2020-05-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurer', '0002_auto_20200519_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='expected',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
