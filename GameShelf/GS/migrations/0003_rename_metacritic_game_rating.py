# Generated by Django 5.0.7 on 2024-09-10 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GS', '0002_game_description_game_metacritic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='metacritic',
            new_name='rating',
        ),
    ]
