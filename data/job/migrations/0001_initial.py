# Generated by Django 4.0.1 on 2022-02-09 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_classification', '0001_initial'),
        ('job_source', '0001_initial'),
        ('location', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('external_id', models.CharField(max_length=256)),
                ('url', models.URLField(max_length=256)),
                ('description', models.TextField(null=True)),
                ('qualifications', models.TextField(null=True)),
                ('evaluations', models.TextField(null=True)),
                ('requirements', models.TextField(null=True)),
                ('required_documents', models.TextField(null=True)),
                ('duties', models.TextField(null=True)),
                ('travel_requirements', models.TextField(null=True)),
                ('education', models.TextField(null=True)),
                ('benefits', models.TextField(null=True)),
                ('benefits_url', models.URLField(null=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('publication_date', models.DateTimeField(null=True)),
                ('application_close_date', models.DateTimeField(null=True)),
                ('how_to_apply', models.TextField(null=True)),
                ('what_to_expect', models.TextField(null=True)),
                ('other_information', models.TextField(null=True)),
                ('telework_eligible', models.BooleanField(null=True)),
                ('supervisory_status', models.BooleanField(null=True)),
                ('drug_test_required', models.BooleanField(null=True)),
                ('relocation_expenses_reimbursed', models.BooleanField(null=True)),
                ('openings', models.IntegerField(null=True)),
                ('department', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_department', to='organization.organization')),
                ('job_classifications', models.ManyToManyField(related_name='%(class)s_relations', to='job_classification.JobClassification')),
                ('job_source', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_relation', to='job_source.jobsource')),
                ('locations', models.ManyToManyField(related_name='%(class)s_relations', to='location.Location')),
                ('organization', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_relation', to='organization.organization')),
            ],
            options={
                'verbose_name': 'job',
                'verbose_name_plural': 'jobs',
                'db_table': 'jobs_job',
                'ordering': ['job_source__name', 'name'],
                'abstract': False,
                'unique_together': {('job_source', 'external_id')},
            },
        ),
    ]
