# Generated by Django 5.1.3 on 2024-12-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_footer_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=100)),
            ],
        ),
    ]