# Generated by Django 4.1 on 2022-08-09 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_alter_photo_id_alter_room_id'),
        ('users', '0002_alter_user_avatar_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favs',
            field=models.ManyToManyField(blank=True, related_name='favs', to='rooms.room'),
        ),
    ]
