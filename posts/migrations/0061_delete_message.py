# Generated by Django 4.2 on 2023-05-08 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0060_offers_button_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='message',
        ),
    ]
