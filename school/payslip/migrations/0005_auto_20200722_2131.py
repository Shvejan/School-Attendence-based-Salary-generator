# Generated by Django 3.0.5 on 2020-07-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payslip', '0004_auto_20200720_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='accNo',
            field=models.BigIntegerField(),
        ),
    ]
