# Generated by Django 3.1.7 on 2021-05-15 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191223_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]