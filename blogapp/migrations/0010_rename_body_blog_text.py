# Generated by Django 5.0.1 on 2024-01-08 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_reguser_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='body',
            new_name='text',
        ),
    ]
