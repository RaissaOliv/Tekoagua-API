# Generated by Django 5.0.4 on 2024-05-08 02:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('company_name', models.CharField()),
                ('cnpj', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('A', 'admin'), ('F', 'employee')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.URLField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TrashLocation',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('latitude', models.CharField()),
                ('longitude', models.CharField()),
                ('city', models.CharField()),
                ('state', models.CharField()),
                ('island', models.CharField()),
                ('country', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyTrashOwner',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tekoagua.company')),
                ('trash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tekoagua.trash')),
            ],
        ),
        migrations.AddField(
            model_name='trash',
            name='trash_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tekoagua.trashlocation'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('password', models.CharField()),
                ('email', models.CharField()),
                ('name', models.CharField()),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tekoagua.company')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tekoagua.profile')),
            ],
        ),
    ]