# Generated by Django 3.2.7 on 2021-10-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='languages',
            field=models.CharField(blank=True, max_length=100, verbose_name='Языки'),
        ),
    ]
