# Generated by Django 4.2.4 on 2023-08-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0004_alter_userprofile_referral_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='freeze_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='total_balance',
            field=models.FloatField(default=0),
        ),
    ]