from django.db import models

class Produit(models.Model):
    Code = models.AutoField(primary_key=True)
    Designation = models.CharField(max_length=100)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    Quantite = models.IntegerField()

class Fournisseur(models.Model):
    Code = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=200)
    Telephone = models.CharField(max_length=20)
    

class Centre(models.Model):
    Code= models.AutoField(primary_key=True)
    Designation = models.CharField(max_length=100)

class Client(models.Model):
    CodeCL = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=200)
    Telephone = models.CharField(max_length=20)
    Credit = models.DecimalField(max_digits=10, decimal_places=2)

class Employe(models.Model):
    Code = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=200)
    Telephone = models.CharField(max_length=20)
    SalaireJ = models.DecimalField(max_digits=10, decimal_places=2)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    
class Masrouf(models.Model):
    
    Date = models.DateField()
    avance = models.DecimalField(max_digits=10, decimal_places=2)
    emp = models.ForeignKey(Employe, on_delete=models.CASCADE)

class Transfer(models.Model):
    
    Date = models.DateField()
    prd = models.ForeignKey(Produit, on_delete=models.CASCADE)
    cntr = models.ForeignKey(Centre, on_delete=models.CASCADE)
    Quantite = models.IntegerField()
    

class Vente(models.Model):
    
    Date = models.DateField()
    prd = models.ForeignKey(Produit, on_delete=models.CASCADE)
    clnt = models.ForeignKey(Client, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=50)

class Achats(models.Model):
    
    Date = models.DateField()
    prd = models.ForeignKey(Produit, on_delete=models.CASCADE)
    frn = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    Montant = models.DecimalField(max_digits=10, decimal_places=2)
    StatutP = models.CharField(max_length=50)
    quantite = models.IntegerField()
    Solde = models.DecimalField(max_digits=10, decimal_places=2)
