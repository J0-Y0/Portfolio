# Generated by Django 5.1.1 on 2024-11-10 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_certifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='certifications',
            name='certificate_link',
            field=models.URLField(default='1'),
            preserve_default=False,
        ),
    ]