# Generated by Django 2.2.1 on 2019-06-22 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0015_auto_20190623_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicleexit',
            old_name='fare',
            new_name='farem',
        ),
    ]
