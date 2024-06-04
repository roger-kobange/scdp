from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titr
    

class User_c(AbstractUser):
    ROLES = (
        ('user', 'Utilisateur'),
        ('admin', 'Administrateur'),
    )
    contact = models.CharField(max_length=100)
    photo_profil = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    def __str__(self):
        return self.username


class Machine(models.Model):
    TYPE_MAINTENANCE_CHOICES = (
        ('jour', 'Jour'),
        ('mois', 'Mois'),
        ('annee', 'Année'),
    )

    nom = models.CharField(max_length=100)
    quantite = models.IntegerField()
    type_maintenance = models.CharField(max_length=5, choices=TYPE_MAINTENANCE_CHOICES)
    description = models.TextField()
    photo = models.ImageField(upload_to='machines_photos/', null=True, blank=True)

    def __str__(self):
        return self.nom
    
class Technicien(User_c):
    fonction = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    pays = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"