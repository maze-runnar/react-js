# Generated by Django 2.2 on 2019-07-07 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190706_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guides',
            name='area',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='guides',
            name='contact',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='guides',
            name='experience',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='guides',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]