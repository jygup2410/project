# Generated by Django 2.2.1 on 2019-06-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_auto_20190610_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mail', models.CharField(default='null', max_length=200)),
                ('contactno', models.CharField(default='', max_length=10)),
                ('question', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]
