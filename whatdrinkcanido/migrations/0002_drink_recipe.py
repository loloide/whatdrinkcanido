# Generated by Django 5.1.2 on 2024-11-28 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatdrinkcanido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='recipe',
            field=models.CharField(default='', max_length=350),
        ),
    ]