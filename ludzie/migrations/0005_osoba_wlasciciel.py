# Generated by Django 4.2.6 on 2023-11-20 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ludzie', '0004_alter_osoba_imie_alter_osoba_miesiac_dodania'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='wlasciciel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
