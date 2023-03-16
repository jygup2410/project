# Generated by Django 2.2.1 on 2019-06-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('contactno', models.CharField(default='', max_length=10)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('address', models.CharField(default='', max_length=200)),
                ('space', models.CharField(default='', max_length=30)),
                ('message', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]
