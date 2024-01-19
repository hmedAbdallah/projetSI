from django import forms
from .models import Fournisseur,Transfer,Produit,Centre

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['Nom', 'Adresse', 'Telephone']





class TransfertMatieresForm(forms.ModelForm):

   
    class Meta:
        model = Transfer
        fields = [
            "Date",
            "prd",
            "cntr",
            "Quantite",
            
        ]

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data["Date"]
        centre = cleaned_data["cntr"]
        produit = cleaned_data["prd"]
        quantite = cleaned_data["QuantiteE"]

        # Vérifier que la quantité est positive
        if quantite < 0:
            raise forms.ValidationError("La quantité doit être positive.")

        

        self.cleaned_data["cout_transfert_equivalent"] = produit.prix_unitaire * quantite

        return cleaned_data

