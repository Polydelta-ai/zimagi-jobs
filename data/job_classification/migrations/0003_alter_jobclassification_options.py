# Generated by Django 3.2.5 on 2021-11-30 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_classification', '0002_alter_jobclassification_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobclassification',
            options={'ordering': ['code'], 'verbose_name': 'job classification', 'verbose_name_plural': 'job classifications'},
        ),
    ]
