# Generated by Django 2.2 on 2019-04-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modele', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Couleur',
            fields=[
                ('Code_Couleur', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Nom_Couleur', models.CharField(max_length=100)),
                ('Hex_Couleur', models.CharField(default='ffffff', max_length=6)),
                ('Colore', models.ManyToManyField(to='modele.Modele')),
            ],
        ),
    ]