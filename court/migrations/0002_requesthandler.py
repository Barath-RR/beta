# Generated by Django 4.0.3 on 2022-09-19 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestHandler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('request_type', models.CharField(max_length=250)),
                ('request_data', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='court.user')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='court.user')),
            ],
        ),
    ]
