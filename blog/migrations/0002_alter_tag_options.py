# Generated by Django 5.1.4 on 2025-01-09 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': 'tags'},
        ),
    ]
