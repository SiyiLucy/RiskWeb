# Generated by Django 4.2.6 on 2023-11-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x1', models.CharField(default='default_value', max_length=100)),
                ('x2', models.CharField(default='default_value', max_length=100)),
                ('x3', models.CharField(default='default_value', max_length=100)),
                ('x4', models.CharField(default='default_value', max_length=100)),
                ('x5', models.CharField(default='default_value', max_length=100)),
                ('x6', models.CharField(default='default_value', max_length=100)),
                ('x7', models.CharField(default='default_value', max_length=100)),
                ('x8', models.CharField(default='default_value', max_length=100)),
                ('x9', models.CharField(default='default_value', max_length=100)),
                ('x10', models.CharField(default='default_value', max_length=100)),
                ('x11', models.CharField(default='default_value', max_length=100)),
                ('x12', models.CharField(default='default_value', max_length=100)),
                ('x13', models.CharField(default='default_value', max_length=100)),
                ('x14', models.CharField(default='default_value', max_length=100)),
                ('x15', models.CharField(default='default_value', max_length=100)),
            ],
        ),
    ]
