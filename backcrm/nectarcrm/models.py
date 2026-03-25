from django.db import models, transaction, IntegrityError
from django.utils import timezone

#Table commun pour les coordonnee
class BaseOlona(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique= True, blank=True, null=True)
    telephone = models.CharField(max_length=10)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)

    STATUT_CHOICES = [
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
        ('archive', 'Archive'),
    ]

    statut = models.CharField(
        max_length=7,
        choices=STATUT_CHOICES,
        default='actif'
    )

    class Meta:
        abstract = True

#generateur fe reference
class ReferenceMixin(models.Model):
    REF_PREFIX = "" #a definir dans chaque model
    REF_FIELD = "ref"

    class Meta:
        abstract = True

    def generate_reference(self):
        zao = timezone.now()
        volana = zao.strftime("%m")
        taona = zao.strftime("%Y")

        prefix_complet = f"{self.REF_PREFIX}{volana}{taona}"

        model_class = self.__class__

        filter_kwargs = {
            f"{self.REF_FIELD}__startswith": prefix_complet
        }

        dernier_obj = model_class.objects.filter(**filter_kwargs).order_by(f'-{self.REF_FIELD}').first()

        if dernier_obj:
            derniere_ref = getattr(dernier_obj, self.REF_FIELD)
            numero = int(derniere_ref.split('-')[-1])
            nouveau_numero = numero +1
        else:
            nouveau_numero = 1

        return f"{prefix_complet}-{nouveau_numero:04d}"
    
    def save(self, *args, **kwargs):
        if not getattr(self, self.REF_FIELD):
            #pour eviter les collisions
            for _ in range(5): #max 5 fois
                try:
                    with transaction.atomic():
                        setattr(self, self.REF_FIELD, self.generate_reference())
                        super().save(*args, **kwargs)
                        return
                except IntegrityError:
                    continue
            raise IntegrityError("Impossible de generer,une ref unique")
        else:
            super().save(*args, **kwargs)

#Gestion des nectarcrm
class Client(BaseOlona, ReferenceMixin):
    REF_PREFIX = "CL"
    GENRE_CHOICES = [
        ('mr', 'Mr'),
        ('mme', 'Mme')
    ]

    id_client = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=10, unique=True, blank=True)
    prenom_client = models.CharField(max_length=100)
    date_naissance_client = models.DateField()
    genre_client = models.CharField(
        max_length=5,
        choices=GENRE_CHOICES,
        default='mr'
    )

    def __str__(self):
        return f"{self.nom} {self.prenom_client} ({self.ref})"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['-date_creation']

#Gestion des fournisseurs
class Fournisseur(BaseOlona, ReferenceMixin):
    REF_PREFIX = "RF"
    TYPE_CHOICES = [
        ('matieres premieres', 'Matieres Premieres'),
        ('inventaire finis', 'Produits Finis'),
        ('services', 'Services'),
        ('equipements', 'Equipements'),
        ('technologies', 'Technologies')
    ]
    PAIEMENT_CHOICES = [
        ('especes', 'Especes'),
        ('cheques', 'Cheques'),
        ('virements bancaires', 'Virements Bancaires'),
        ('mobile money', 'Mobile Money')
    ]

    id_fournisseur = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=10, unique=True, blank=True)
    nom_entreprise = models.CharField(max_length=100, blank=True)
    type_fournisseur = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='matières premières'
    )
    moyen_de_paiement = models.CharField(
        max_length=20,
        choices=PAIEMENT_CHOICES,
        default='espèces'
    )

    def __str__(self):
        return f"{self.nom} {self.nom_entreprise} ({self.ref})"

    class Meta:
        verbose_name = "Fournisseur"
        verbose_name_plural = "Fournisseurs"
        ordering = ['-date_creation']
