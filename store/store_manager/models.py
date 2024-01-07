from django.db import models

class Produit(models.Model):
    CodeP = models.AutoField(primary_key=True)
    Designation = models.CharField(max_length=100)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    Quantite = models.IntegerField()

class Fournisseur(models.Model):
    CodeF = models.AutoField(primary_key=True)
    NomF = models.CharField(max_length=100)
    AdresseF = models.CharField(max_length=200)
    TelephoneF = models.CharField(max_length=20)
    Solde = models.DecimalField(max_digits=10, decimal_places=2)

class Centre(models.Model):
    CodeCNTR = models.AutoField(primary_key=True)
    DesignationC = models.CharField(max_length=100)

class Client(models.Model):
    CodeCL = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=200)
    Telephone = models.CharField(max_length=20)
    Credit = models.DecimalField(max_digits=10, decimal_places=2)

class Employe(models.Model):
    CodeEMP = models.AutoField(primary_key=True)
    NomE = models.CharField(max_length=100)
    AdresseE = models.CharField(max_length=200)
    TelephoneE = models.CharField(max_length=20)
    SalaireJ = models.DecimalField(max_digits=10, decimal_places=2)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    
class Masrouf(models.Model):
    
    DateM = models.DateField()
    avanceS = models.DecimalField(max_digits=10, decimal_places=2)
    emp = models.ForeignKey(Employe, on_delete=models.CASCADE)

class Transfer(models.Model):
    
    Date = models.DateField()
    prd = models.ForeignKey(Produit, on_delete=models.CASCADE)
    cntr = models.ForeignKey(Centre, on_delete=models.CASCADE)
    QuantiteE = models.IntegerField()
    coutE = models.DecimalField(max_digits=10, decimal_places=2)

class Vente(models.Model):
    
    DateV = models.DateField()
    prd = models.ForeignKey(Produit, on_delete=models.CASCADE)
    clnt = models.ForeignKey(Client, on_delete=models.CASCADE)
    montantV = models.DecimalField(max_digits=10, decimal_places=2)
    statutPY = models.CharField(max_length=50)

class Achats(models.Model):
    
    DateA = models.DateField()
    prd = models.ForeignKey(Produit, on_delete=models.CASCADE)
    frn = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    Montant = models.DecimalField(max_digits=10, decimal_places=2)
    StatutP = models.CharField(max_length=50)
    quantiteA = models.IntegerField()
