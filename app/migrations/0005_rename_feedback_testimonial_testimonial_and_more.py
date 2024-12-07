# Generated by Django 5.1.3 on 2024-12-06 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_service_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='feedback',
            new_name='testimonial',
        ),
        migrations.RemoveField(
            model_name='beautician',
            name='bio',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]