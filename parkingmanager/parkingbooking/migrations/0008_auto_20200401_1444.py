# Generated by Django 2.2.5 on 2020-04-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingbooking', '0007_auto_20200401_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercar',
            name='car_image',
            field=models.ImageField(null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='usercar',
            name='plate',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
