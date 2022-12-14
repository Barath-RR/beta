# Generated by Django 4.0.3 on 2022-09-19 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0002_requesthandler'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('assigned_advocate', models.CharField(max_length=250)),
                ('affidavit', models.CharField(max_length=250)),
                ('charge_sheet', models.CharField(max_length=250)),
                ('casefiles', models.CharField(max_length=250)),
                ('case_status', models.CharField(default='Not yet assigned', max_length=250)),
                ('severity_index', models.CharField(default='0.1', max_length=250)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='court.user')),
            ],
        ),
    ]
