# Generated by Django 4.1.2 on 2023-01-22 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_imagesearch_options_alter_textsearch_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesearch',
            options={'ordering': ('time',)},
        ),
        migrations.AlterModelOptions(
            name='textsearch',
            options={'ordering': ('time',)},
        ),
    ]