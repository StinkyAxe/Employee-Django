# Generated by Django 3.0.7 on 2020-06-29 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('father_name', models.CharField(max_length=20)),
                ('mother_name', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('ephone', models.IntegerField()),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('flat_number', models.IntegerField()),
                ('flat_name', models.CharField(max_length=20)),
                ('landmark', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]