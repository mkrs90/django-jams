# Generated by Django 4.2 on 2023-04-05 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tunes', '0007_song_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(help_text='Select an song for this playlist', to='tunes.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tunes.album'),
        ),
    ]
