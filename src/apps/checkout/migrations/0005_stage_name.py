# Generated by Django 3.1.6 on 2021-02-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20210213_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='name',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]