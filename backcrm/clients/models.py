from django.db import models

class Client(models.Model):
    SEXE_CHOICES = [
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ]

    id_client = models.AutoField(primary_key=True)
    nom_client = models.CharField(max_length=100)
    prenom_client = models.CharField(max_length=100)
    date_naissance_client = models.DateField()
    sexe_client = models.CharField(
        max_length=5,
        choices=SEXE_CHOICES,
        default='homme'
    )
    email_client = models.EmailField(unique=True, blank=True, null=True)
    telephone_client = models.CharField(max_length=20)
    adresse_client = models.CharField(max_length=200)
    ville_client = models.CharField(max_length=100)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
