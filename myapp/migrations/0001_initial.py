# Generated by Django 4.1.2 on 2023-01-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrackerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastupdated', models.BigIntegerField()),
                ('renderingtext', models.BooleanField(default=True)),
                ('imageCount', models.IntegerField()),
                ('renderingImage', models.BooleanField(default=True)),
            ],
        ),
    ]
