from django.shortcuts import render
from datetime import date
from .serializers import ProduitSerializer
from rest_framework import viewsets
from .forms import FournisseurForm
from .models import Produit, Achats

def etat_stock(request):
    # Filtrer les produits en fonction des achats
    achats = Achats.objects.all()
    produits = Produit.objects.all()
    # Récupération des paramètres de filtre s'ils sont présents dans la requête GET
    fournisseur = request.GET.get('fournisseur')
    date_achat = request.GET.get('date_achat')
    nom_matiere = request.GET.get('nom_matiere')


    # Appliquer les filtres s'ils sont définis

    if fournisseur:
        achats = achats.filter(frn=fournisseur)
    
    if date_achat:
        achats = achats.filter(DateA=date_achat)
    if nom_matiere:
        produits = produits.filter(Designation=nom_matiere) 

    # Récupérer les produits associés aux achats filtrés
    filltredProduits = [achat.prd for achat in achats if achat.prd in produits]

    # Calculer la valeur totale du stock
    valeur_totale_stock = sum(achat.Montant for achat in achats)

    
    return render(request, 'stock.html', {
        'produits': filltredProduits,
        'valeur_totale_stock': valeur_totale_stock
    })

from django.shortcuts import render, redirect
from .models import Produit, Fournisseur, Achats

def achat_matiere(request):
    fournisseurs = Fournisseur.objects.all()
    produits = Produit.objects.all()

    if request.method == 'POST':
        fournisseur = fournisseurs.get(CodeF=request.POST.get('fournisseur_nom'))
        produit = produits.get(CodeP=request.POST.get('produit_nom'))
        quantite = int(request.POST.get('quantite'))
        prix_unitaire = float(request.POST.get('prix_unitaire'))
        

        # Calcul du montant total de l'achat
        montant_achat = quantite * prix_unitaire

        # Création d'une entrée dans la table Achats
        nouvel_achat = Achats(
            DateA = date.today(),
            prd=produit,
            frn= fournisseur,
            Montant=montant_achat,
            StatutP='En attente',  # Vous pouvez ajuster le statut selon vos besoins
            quantiteA=quantite
        )
        nouvel_achat.save()

        return redirect('confirmation_achat')  # Redirection vers la page de confirmation

    return render(request, 'achat_matiere.html', {'fournisseurs': fournisseurs, 'produits': produits})



def achats_confirmation(request):
    return render(request, 'achats_confirmation.html')

def fournisseur_form_view(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock')  
    else:
        form = FournisseurForm()
    return render(request, 'creerFournisseur.html', {'form': form})



class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer


