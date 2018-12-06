from django.db import models

# Create your models here.
class Eleve(models.Model):
    nom_complet = models.CharField(max_length=50)
    niveau_etude = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
   
   
