# Generated by Django 5.1 on 2025-01-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0013_alter_blogpost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
