# Generated by Django 4.2.4 on 2023-08-28 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_creator_options_alter_car_last_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': ('Car',), 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': ('Comment',), 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='countries',
            options={'verbose_name': ('Country',), 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='creator',
            options={'verbose_name': ('Creator',), 'verbose_name_plural': 'Creators'},
        ),
    ]
