# Generated by Django 5.0.1 on 2024-01-07 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog_reguser_delete_myuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.CharField(max_length=10000),
        ),
    ]
