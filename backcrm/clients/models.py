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