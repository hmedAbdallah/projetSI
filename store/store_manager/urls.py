from django.urls import path,include
from . import views
from rest_framework import routers
from .views import ProduitViewSet

router = routers.DefaultRouter()
router.register(r'produits', ProduitViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('magasin/stock',views.etat_stock, name='stock'),
    path('magasin/achats',views.achat_matiere, name='achats'),
    path('magasin/achats_confirmation',views.achats_confirmation,name="confirmation_achat"),
    path('magasin/ajouter_fournisseur',views.fournisseur_form_view, name="ajoutfrn")
]