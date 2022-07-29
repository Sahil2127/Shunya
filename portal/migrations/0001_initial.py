# Generated by Django 3.1 on 2020-10-03 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=300)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.class')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('url', models.URLField(blank=True, default='', max_length=300)),
                ('upload', models.FileField(upload_to=None)),
                ('chapter_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.class'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='subject_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.subject'),
        ),
    ]