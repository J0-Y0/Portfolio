# Generated by Django 5.1.1 on 2024-11-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0008_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='skill_logos/'),
        ),
    ]
