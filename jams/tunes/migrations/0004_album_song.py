# Generated by Django 4.2 on 2023-04-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunes', '0003_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('published_date', models.DateField()),
                ('cover_art', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
