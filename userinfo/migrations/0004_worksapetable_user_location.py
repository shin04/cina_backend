# Generated by Django 3.0.5 on 2020-05-23 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_auto_20200424_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksapetable',
            name='user_location',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]