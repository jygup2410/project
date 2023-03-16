
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='addressfor',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='registration',
            name='contactnumber',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='registration',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.EmailField(default='null', max_length=254),
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='male', max_length=10),
        ),
        migrations.AddField(
            model_name='registration',
            name='passwordr',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='registration',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
    ]
