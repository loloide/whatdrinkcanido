# Generated by Django 5.1.2 on 2024-11-28 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatdrinkcanido', '0003_alter_drink_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='recipe',
            field=models.TextField(),
        ),
    ]