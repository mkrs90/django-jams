# Generated by Django 4.2 on 2023-04-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunes', '0006_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(help_text='Select an artist for this song', to='tunes.artist'),
        ),
    ]
