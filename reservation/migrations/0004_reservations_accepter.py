# Generated by Django 2.2 on 2019-09-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_vehicule_vendu'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='accepter',
            field=models.BooleanField(default=False),
        ),
    ]
