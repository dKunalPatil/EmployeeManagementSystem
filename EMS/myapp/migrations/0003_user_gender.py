# Generated by Django 3.2.5 on 2021-08-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_mobile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('0', 'Female'), ('1', 'male')], default='sex', max_length=11),
        ),
    ]
