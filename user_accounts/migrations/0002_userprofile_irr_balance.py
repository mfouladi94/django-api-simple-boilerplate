# Generated by Django 4.2.4 on 2023-08-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='irr_balance',
            field=models.FloatField(default=0),
        ),
    ]