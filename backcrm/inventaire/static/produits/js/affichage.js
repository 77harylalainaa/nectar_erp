document.addEventListener("DOMContentLoaded", function () {
    const lignes = document.querySelectorAll(".ligne-produit");
    const form = document.querySelector(".form-produit");
    const idInput = document.getElementById("id_produit");
    const submitBtn = document.getElementById("submit-btn");
    const resetBtn = document.querySelector(".btn-boot");

    lignes.forEach(ligne => {
        ligne.addEventListener("click", function () {
            // on recupere les data
            const data = this.dataset;

            //on retire la surbrillance de toutes les lignes
            lignes.forEach(l => l.classList.remove("active"));

            // ajout du surbrillance sur la ligne cliquée
            this.classList.add("active");

            // on rempli le formulaire
            idInput.value = data.id;
            document.getElementById("id_reference").value = data.reference;
            document.getElementById("id_nom_produit").value = data.nom_produit;
            document.getElementById("id_categorie").value = data.categorie;
            document.getElementById("id_marque").value = data.marque;
            document.getElementById("id_format").value = data.format;
            document.getElementById("id_fournisseur").value = data.fournisseur;
            document.getElementById("id_prix_d_achat").value = data.prix_d_achat;
            document.getElementById("id_prix_de_vente").value = data.prix_de_vente;
            document.getElementById("id_remise_possible").value = data.remise_possible;
            document.getElementById("id_statut").value = data.statut;
            document.getElementById("id_description").value = data.description;

            // ici on change le bouton
            submitBtn.innerHTML = "<span class='icon'> Modifier </span>";
        });
    });

    resetBtn.addEventListener("click", function () {
        form.reset();
        idInput.value = "";
        lignes.forEach(l => l.classList.remove("active"));
        submitBtn.innerHTML = "<span class='icon'> Ajouter </span>";
    });
});