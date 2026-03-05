from django.db import models

class Produit(models.Model):
    STATUT_CHOICES = [
        ('disponible', 'Disponible'),
        ('non_disponible', 'Non disponible'),
        ('archivé', 'Archivé'),
    ]
    CATEGORIE_CHOICES = [
        ('rhum', 'Rhum'),
        ('vin', 'Vin'),
        ('spiritueux', 'Spiritueux'),
        ('bière', 'Bière'),
        ('boisson_gazeuse', 'Boisson gazeuse'),
        ('jus_de_fruit', 'Jus de fruit')
    ]
    FORMAT_CHOICES = [
        ('25cl', '25cl'),
        ('33cl', '33cl'),
        ('50cl', '50cl'),
        ('70cl', '70cl'),
        ('100cl', '100cl'),
    ]

    id_produit = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=100, unique=True)
    nom_produit = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    categorie = models.CharField(
        max_length=20,
        choices=CATEGORIE_CHOICES,
        default='rhum'
    )
    marque = models.CharField(max_length=150)
    fournisseur = models.CharField(max_length=150)
    prix_d_achat= models.DecimalField(max_digits=10, decimal_places=2)
    prix_de_vente = models.DecimalField(max_digits=10, decimal_places=2)
    remise_possible = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Pourcentege de remise possible"
    )
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='disponible'
    )
    format = models.CharField(
        max_length=100,
        choices=FORMAT_CHOICES,
        default='70cl'
    )
    date_de_creation = models.DateTimeField(auto_now_add=True)
    image_produit = models.ImageField(
        upload_to='produits/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.nom_produit} ({self.reference})"

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['-date_de_creation']
