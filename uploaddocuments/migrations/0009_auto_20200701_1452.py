# Generated by Django 3.0.7 on 2020-07-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploaddocuments', '0008_auto_20200701_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddocuments',
            name='photo',
            field=models.ImageField(upload_to='media/%Y/%m/%d/'),
        ),
    ]
