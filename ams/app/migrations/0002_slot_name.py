# Generated by Django 3.2.6 on 2021-10-18 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]