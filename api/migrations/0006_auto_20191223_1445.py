# Generated by Django 2.2.1 on 2019-12-23 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191223_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchingforworker',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='matchforworker_worker', to='users.Worker'),
        ),
    ]