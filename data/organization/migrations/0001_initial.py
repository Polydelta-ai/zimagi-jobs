# Generated by Django 3.2.5 on 2021-11-22 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('locations', models.ManyToManyField(related_name='organization_relations', to='location.Location')),
                ('parent', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organization_relation', to='organization.organization')),
            ],
            options={
                'verbose_name': 'organization',
                'verbose_name_plural': 'organizations',
                'db_table': 'jobs_organization',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]