# Generated by Django 5.0.1 on 2024-01-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_remove_blog_image_alter_blog_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='reguser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
