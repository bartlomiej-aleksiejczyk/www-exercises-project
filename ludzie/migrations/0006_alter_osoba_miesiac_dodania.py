# Generated by Django 4.2.6 on 2023-12-04 12:48

from django.db import migrations, models
import ludzie.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ludzie', '0005_osoba_wlasciciel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='miesiac_dodania',
            field=models.CharField(default='December', max_length=213, validators=[ludzie.validators.czy_nie_przyszlosc_miesiac]),
        ),
    ]
