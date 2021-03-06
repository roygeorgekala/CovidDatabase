# Generated by Django 3.0.7 on 2020-12-11 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_hospital_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=15),
        ),
        migrations.CreateModel(
            name='Close_Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='John Doe', max_length=256)),
                ('relation', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=256)),
                ('test_status', models.CharField(max_length=3)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Patient')),
            ],
        ),
    ]
