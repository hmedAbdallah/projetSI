import axios from "axios";

// Récupérer la liste des produits
axios
  .get("/api/produits")
  .then((response) => {
    const produits = response.data;

    // Créer une liste pour afficher les noms de produits
    const listeProduits = document.createElement("ul");

    // Ajouter chaque nom de produit à la liste
    produits.forEach((produit) => {
      const item = document.createElement("li");
      item.textContent = produit.nom; // En supposant que le champ nom contient le nom du produit
      listeProduits.appendChild(item);
    });

    // Ajouter la liste à la page
    document.body.appendChild(listeProduits);
  })
  .catch((error) => {
    console.error(error);
  });
