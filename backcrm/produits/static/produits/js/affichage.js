document.addEventListener("DOMContentLoaded", function () {
    const lignes = document.querySelectorAll(".ligne-produit");
    const idInput = document.getElementById("id_produit");
    const submitBtn = document.getElementById("submit-btn");
    const resetBtn = document.querySelector(".btn-boot");

    lignes.forEach(ligne => {
        ligne.addEventListener("click", function () {
            // ici on recupere les data
            const id = this.dataset.id;
            const reference = this.dataset.reference;
            const nom_produit = this.dataset.nom_produit;
            const categorie = this.dataset.categorie;
            const marque = this.dataset.marque;
            const format = this.dataset.format;
            const fournisseur = this.dataset.fournisseur;
            const prix_d_achat = this.dataset.prix_d_achat;
            const prix_de_vente = this.dataset.prix_de_vente;
            const remise_possible = this.dataset.remise_possible;
            const statut = this.dataset.statut;
            const image_produit = this.dataset.image_produit;
            const description = this.dataset.description;

            // ici on rempli le formulaire
            idInput.value = id;
            document.getElementById("id_reference").value = reference;
            document.getElementById("id_nom_produit").value = nom_produit;
            document.getElementById("id_categorie").value = categorie;
            document.getElementById("id_marque").value = marque;
            document.getElementById("id_format").value = format;
            document.getElementById("id_fournisseur").value = fournisseur;
            document.getElementById("id_prix_d_achat").value = prix_d_achat;
            document.getElementById("id_prix_de_vente").value = prix_de_vente;
            document.getElementById("id_remise_possible").value = remise_possible;
            document.getElementById("id_statut").value = statut;
            document.getElementById("id_image_produit").value = image_produit;
            document.getElementById("id_description").value = description;

            // ici on change le bouton
            submitBtn.innerHTML = "<span class='icon'> Modifier </span>";
        });
    });

    resetBtn.addEventListener("click", function () {
        idInput.value = "";
        submitBtn.innerHTML = "<span class='icon'> Ajouter </span>";
    });
});