# Generated by Django 2.2.1 on 2019-07-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stone',
            name='x1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='stone',
            name='x2',
            field=models.CharField(max_length=10),
        ),
    ]