from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.parent} ({self.nom})"
class Produit(models.Model):
    STATUT_CHOICES = [
        ('disponible', 'Disponible'),
        ('non_disponible', 'Non Disponible'),
        ('archive', 'Archive'),
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
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    marque = models.CharField(max_length=150)
    fournisseur = models.ForeignKey(
        "nectarcrm.Fournisseur",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
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
        upload_to='inventaire/',
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.reference:
            dernier_produit = Produit.objects.order_by('-id_produit').first()
            if dernier_produit and dernier_produit.reference:
                numero = ''.join(filter(str.isdigit, dernier_produit.reference))
                dernier_numero = int(numero) if numero else 0
                nouveau_numero = dernier_numero + 1
            else:
                nouveau_numero = 1
            self.reference = f"PR{nouveau_numero:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom_produit} ({self.reference})"

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['-date_de_creation']

class Stock(models.Model):
    produit = models.OneToOneField(
        Produit,
        on_delete=models.CASCADE,
        related_name="stock"
    )
    quantite = models.IntegerField(default=0)
    dernier_maj = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.produit.nom_produit} - Stock: {self.quantite}"

class MouvementStock(models.Model):
    TYPE_CHOICES = [
        ('entree', 'Entree'),
        ('sortie', 'Sortie'),
    ]

    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    type_mouvement = models.CharField(max_length=10, choices=TYPE_CHOICES)
    quantite = models.IntegerField()
    date_mouv = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.type_mouvement} - {self.produit.nom_produit} ({self.quantite})"
