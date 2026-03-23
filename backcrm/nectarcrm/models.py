from django.db import models

class Client(models.Model):
    GENRE_CHOICES = [
        ('mr', 'Mr'),
        ('mme', 'Mme')
    ]
    ETAT_CHOICES = [
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
        ('archivé', 'Archivé'),
    ]

    id_client = models.AutoField(primary_key=True)
    ref_client = models.CharField(max_length=50, unique=True, blank=True)
    nom_client = models.CharField(max_length=100)
    prenom_client = models.CharField(max_length=100)
    date_naissance_client = models.DateField()
    genre_client = models.CharField(
        max_length=5,
        choices=GENRE_CHOICES,
        default='mr'
    )
    email_client = models.EmailField(unique=True, blank=True, null=True)
    telephone_client = models.CharField(max_length=20)
    adresse_client = models.CharField(max_length=200)
    ville_client = models.CharField(max_length=100)
    date_inscription = models.DateTimeField(auto_now_add=True)
    etat_client = models.CharField(
        max_length= 10,
        choices=ETAT_CHOICES,
        default='actif'
    )

    def save(self, *args, **kwargs):
        if not self.ref_client:
            dernier_client = Client.objects.order_by('-id_client').first()
            if dernier_client and dernier_client.ref_client:
                numero = ''.join(filter(str.isdigit, dernier_client.ref_client))
                dernier_numero = int(numero) if numero else 0
                nouveau_numero = dernier_numero + 1
            else:
                nouveau_numero = 1
            self.ref_client = f"CL{nouveau_numero:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom_client} ({self.ref_client})"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['-date_inscription']

class Fournisseur(models.Model):
    TYPE_CHOICES = [
        ('matières premières', 'Matières Premières'),
        ('produits finis', 'Produits Finis'),
        ('services', 'Services'),
        ('équipements', 'Equipements'),
        ('technologies', 'Technologies')
    ]
    PAIEMENT_CHOICES = [
        ('espèces', 'Espèces'),
        ('chèques', 'Chèques'),
        ('virements bancaires', 'Virements Bancaires'),
        ('mobile money', 'Mobile Money')
    ]
    ACTIVITE_CHOICES = [
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
        ('archivé', 'Archivé')
    ]

    id_fournisseur = models.AutoField(primary_key=True)
    ref_fournisseur = models.CharField(max_length=10, unique=True, blank=True)
    nom_fournisseur = models.CharField(max_length=100)
    nom_entreprise = models.CharField(max_length=100, blank=True)
    type_fournisseur = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='matières premières'
    )
    email_fournisseur = models.EmailField(unique=True, blank=True, null=True)
    telephone_fournisseur = models.CharField(max_length=15)
    adresse_fournisseur = models.CharField(max_length=150)
    ville_fournisseur = models.CharField(max_length=50)
    date_ajout = models.DateTimeField(auto_now_add=True)
    moyen_de_paiement = models.CharField(
        max_length=20,
        choices=PAIEMENT_CHOICES,
        default='espèces'
    )
    activite_fournisseur = models.CharField(
        max_length=10,
        choices=ACTIVITE_CHOICES,
        default='actif'
    )

    def save(self, *args, **kwargs):
        if not self.ref_fournisseur:
            dernier_fournisseur = Fournisseur.objects.order_by('-id_fournisseur').first()
            if dernier_fournisseur and dernier_fournisseur.ref_fournisseur:
                numero = ''.join(filter(str.isdigit, dernier_fournisseur.ref_fournisseur))
                dernier_numero = int(numero) if numero else 0
                nouveau_numero = dernier_numero + 1
            else:
                nouveau_numero = 1
            self.ref_fournisseur = f"RF{nouveau_numero:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ref_fournisseur} ({self.nom_fournisseur})"

    class Meta:
        verbose_name = "Fournisseur"
        verbose_name_plural = "Fournisseurs"
        ordering = ['-date_ajout']
