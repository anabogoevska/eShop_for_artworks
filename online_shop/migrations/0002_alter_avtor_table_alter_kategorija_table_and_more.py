# Generated by Django 4.0.5 on 2022-12-27 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='avtor',
            table='"online_prodavnica". "avtor"',
        ),
        migrations.AlterModelTable(
            name='kategorija',
            table='"online_prodavnica". "kategorija"',
        ),
        migrations.AlterModelTable(
            name='kupuvac',
            table='"online_prodavnica". "kupuvac"',
        ),
        migrations.AlterModelTable(
            name='kupuvac_kupuva_umetnicko_delo',
            table='"online_prodavnica". "kupuvac_kupuva_umetnicko_delo"',
        ),
        migrations.AlterModelTable(
            name='naracka',
            table='"online_prodavnica". "naracka"',
        ),
        migrations.AlterModelTable(
            name='posetitel_na_aplikacijata',
            table='"online_prodavnica". "posetitel_na_aplikacijata"',
        ),
        migrations.AlterModelTable(
            name='umetnicko_delo',
            table='"online_prodavnica". "umetnicko_delo"',
        ),
    ]