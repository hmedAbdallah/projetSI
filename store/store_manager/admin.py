from django.contrib import admin

from .models import Produit, Fournisseur, Centre,Client, Employe,Masrouf,Transfer,Vente,Achats

admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Centre)
admin.site.register(Client)
admin.site.register(Employe)
admin.site.register(Masrouf)
admin.site.register(Transfer)
admin.site.register(Vente)
admin.site.register(Achats)

