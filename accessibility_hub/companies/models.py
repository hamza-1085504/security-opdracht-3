from django.db import models
from django.contrib.auth.models import AbstractUser
from administrators.models import Ervaringsdeskundige

# Create your models here.


class Organisatie(AbstractUser):
    bedrijfsnaam = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, db_column='email')
    token = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255, default='Nieuw')
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'organisaties'


class Onderzoek(models.Model):
    onderzoek_id = models.AutoField(primary_key=True)
    titel = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255, default='Nieuw')
    beschikbaar = models.BooleanField(default=True)
    beschrijving = models.TextField()
    startdatum = models.DateField()
    einddatum = models.DateField()
    type_onderzoek = models.CharField(max_length=255)
    locatie = models.CharField(max_length=255)
    met_beloning = models.BooleanField(default=False)
    beloning = models.CharField(max_length=255, blank=True, null=True)
    doelgroep_leeftijd_van = models.IntegerField()
    doelgroep_leeftijd_tot = models.IntegerField()
    doelgroep_beperking = models.CharField(max_length=255)
    organisatie = models.ForeignKey(Organisatie, on_delete=models.CASCADE, related_name='onderzoeken')
    deskundige = models.ForeignKey(Ervaringsdeskundige, on_delete=models.CASCADE, related_name='ervaringsdeskundigen')

    class Meta:
        db_table = 'onderzoeken'


class Vraag(models.Model):
    vraag_id = models.AutoField(primary_key=True)
    vraagtitel = models.CharField(max_length=255)
    beschrijving = models.TextField()
    categorie = models.CharField(max_length=255)
    onderzoek = models.ForeignKey(Onderzoek, on_delete=models.CASCADE, related_name='vragen')

    class Meta:
        db_table = 'vragen'
