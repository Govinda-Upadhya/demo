# Generated by Django 5.0.4 on 2024-07-02 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0007_career'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('hiring_process', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(max_length=200)),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirement', to='APP.announcement')),
            ],
        ),
    ]