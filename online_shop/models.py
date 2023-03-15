from django.db import models

# Create your models here.


class kategorija(models.Model):

    id_na_kategorija = models.AutoField(primary_key=True)
    ime_na_kategorija = models.CharField(max_length=30, null=False)

    class Meta:
        managed = False
        db_table =  '"online_prodavnica". "kategorija"'




class posetitel_na_aplikacijata(models.Model):
    id_na_posetitel = models.AutoField(primary_key=True)
    ime = models.CharField(max_length=150, null=False)
    prezime = models.CharField(max_length=150, null=False)
    e_mail_adresa = models.CharField(max_length=150, null=False)
    username = models.CharField(max_length=150, null=False)
    password = models.CharField(max_length=150, null=False)
    telefonski_broj = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = '"online_prodavnica". "posetitel_na_aplikacijata"'


class kupuvac(models.Model):
    id_na_posetitel = models.ForeignKey(posetitel_na_aplikacijata, on_delete=models.CASCADE, primary_key=True, db_column='id_na_posetitel')
    drzava = models.CharField(max_length=100, null=False)
    grad = models.CharField(max_length=100, null=False)
    ulica = models.CharField(max_length=100, null=False)
    broj = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = '"online_prodavnica". "kupuvac"'


class avtor(models.Model):
    id_na_posetitel = models.ForeignKey(posetitel_na_aplikacijata, on_delete=models.CASCADE, primary_key=True, db_column='id_na_posetitel')

    class Meta:
        managed = False
        db_table = '"online_prodavnica". "avtor"'

class umetnicko_delo(models.Model):
    id_na_umetnicko_delo = models.AutoField(primary_key=True)
    ime_na_umetnicko_delo = models.CharField(max_length=100, null=False)
    dimenzija = models.CharField(max_length=100, null=False)
    cena = models.CharField(max_length=100, null=False)
    slika_od_umetnicko_delo = models.CharField(max_length=100, null=False)
    id_avtor = models.ForeignKey(avtor, on_delete=models.CASCADE, null=False, db_column='id_avtor')
    id_na_kategorija = models.ForeignKey(kategorija, on_delete=models.CASCADE, null=False, db_column='id_na_kategorija')

    class Meta:
        managed = False
        db_table = '"online_prodavnica". "umetnicko_delo"'


class naracka(models.Model):
    id_naracka = models.AutoField(primary_key=True)
    tip = models.CharField(max_length=100, null=False)
    opis = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=100, null=False)
    datum = models.DateTimeField(null=False)
    id_na_umetnicko_delo = models.ForeignKey(umetnicko_delo, on_delete=models.CASCADE, db_column='id_na_umetnicko_delo')
    id_kupuvac = models.ForeignKey(kupuvac, on_delete=models.CASCADE, db_column='id_kupuvac')
    id_avtor = models.ForeignKey(avtor, on_delete=models.CASCADE, db_column='id_avtor')

    class Meta:
        managed = False
        db_table = '"online_prodavnica". "naracka"'

class kupuvac_kupuva_umetnicko_delo(models.Model):
    id_kupuvac = models.ForeignKey(kupuvac, primary_key=True,  on_delete=models.CASCADE,  db_column='id_kupuvac')
    id_na_umetnicko_delo = models.ForeignKey(umetnicko_delo, on_delete=models.CASCADE, db_column='id_na_umetnicko_delo')
    datum = models.DateTimeField(null=False)

    class Meta:
        managed = False
        db_table = '"online_prodavnica". "kupuvac_kupuva_umetnicko_delo"'


