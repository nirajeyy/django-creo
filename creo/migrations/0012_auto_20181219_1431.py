# Generated by Django 2.1.2 on 2018-12-19 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creo', '0011_auto_20181219_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsubmission',
            name='publisher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]