# Generated by Django 2.1.5 on 2019-02-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='date_commissioned',
            field=models.DateField(blank=True),
        ),
    ]