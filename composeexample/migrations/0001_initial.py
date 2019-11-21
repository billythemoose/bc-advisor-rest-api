# Generated by Django 2.2.7 on 2019-11-06 18:11

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('cid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('pid', models.IntegerField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='composeexample.College')),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='IProgram',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('pid', models.IntegerField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='composeexample.Fields')),
            ],
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('classes', django.contrib.postgres.fields.jsonb.JSONField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='composeexample.IProgram')),
            ],
        ),
        migrations.CreateModel(
            name='ClassesQ',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='composeexample.Classes')),
                ('quarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='composeexample.Quarter')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='composeexample.Fields'),
        ),
    ]
