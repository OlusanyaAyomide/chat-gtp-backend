# Generated by Django 4.1.2 on 2023-01-18 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackermodel',
            name='textcount',
            field=models.IntegerField(null=True),
        ),
    ]
