# Generated by Django 3.0.5 on 2020-04-24 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worksapetable',
            old_name='Workspace',
            new_name='workspace',
        ),
        migrations.AddField(
            model_name='workspace',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
