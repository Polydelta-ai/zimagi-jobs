# Generated by Django 3.2.5 on 2021-11-22 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default=1, editable=False, max_length=256),
            preserve_default=False,
        ),
    ]
