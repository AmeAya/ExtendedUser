# Generated by Django 4.2.3 on 2023-07-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='social_page',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]