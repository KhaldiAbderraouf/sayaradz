# Generated by Django 2.2 on 2019-04-10 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='Image',
            field=models.ImageField(blank=True, default='version/default.png', upload_to='version'),
        ),
    ]