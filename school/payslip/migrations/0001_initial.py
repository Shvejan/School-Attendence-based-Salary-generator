# Generated by Django 3.0.5 on 2020-07-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('pan', models.CharField(max_length=100)),
                ('accNo', models.IntegerField()),
                ('pfNo', models.CharField(max_length=100)),
                ('esiNo', models.CharField(max_length=100)),
                ('uan', models.CharField(max_length=100)),
                ('leaves_allowed', models.CharField(max_length=100)),
                ('join_date', models.DateField()),
                ('basic', models.CharField(max_length=100)),
            ],
        ),
    ]