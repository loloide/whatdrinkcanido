# Generated by Django 5.1.2 on 2024-11-29 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatdrinkcanido', '0004_alter_drink_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drink',
            old_name='cover_image',
            new_name='image',
        ),
    ]
