# Generated by Django 4.1.2 on 2023-01-22 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_imagesearch_textsearch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesearch',
            options={'ordering': ('-time',)},
        ),
        migrations.AlterModelOptions(
            name='textsearch',
            options={'ordering': ('-time',)},
        ),
    ]
