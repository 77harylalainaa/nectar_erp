document.addEventListener("DOMContentLoaded", function () {

    const lignes = document.querySelectorAll("[data-ligne]");
    const form = document.querySelector("[data-form]");
    const idInput = document.querySelector("[data-id-field]");
    const submitBtn = document.getElementById("submit-btn");
    const resetBtn = document.querySelector(".btn-boot");
    const container = document.querySelector(".kotonera");
    const addBtn = document.getElementById("btn-add");
    const closeBtn = document.getElementById("btn-close");

    /* bouton + : ouvrir formulaire vide */

    if(addBtn){
        addBtn.addEventListener("click", function(){
            container.classList.add("form-open");
            if(form){
                form.reset();
            }
            if(idInput){
                idInput.value = "";
            }
            if(submitBtn){
                submitBtn.innerHTML = "<span class='icon'> Ajouter </span>";
            }
            lignes.forEach(l => l.classList.remove("active"));
        });
    }

    /* clic ligne tableau */

    if (lignes && lignes.length > 0) {
        lignes.forEach(function(ligne){
            ligne.addEventListener("click", function () {
                const data = this.dataset;

                container.classList.add("form-open");

                lignes.forEach(function(l){
                    l.classList.remove("active");
                });
                this.classList.add("active");

                if (idInput && data.id){
                    idInput.value = data.id;
                }

                Object.keys(data).forEach(function(key){
                    const field = document.getElementById("id_" + key);
                    if (field){
                        if(field.type === "file") return;
                        field.value = data[key];
                    }
                });

                if (submitBtn){
                    submitBtn.innerHTML = "<span class='icon'> Modifier </span>";
                }
            });
        });
    }

    /* reset */

    if(resetBtn){
        resetBtn.addEventListener("click", function () {
            if(form){
                form.reset();
            }
            if (idInput){
                idInput.value = "";
            }
            lignes.forEach(function(l){
                l.classList.remove("active");
            });
            if (submitBtn){
                submitBtn.innerHTML = "<span class='icon'> Ajouter </span>";
            }
        });
    }

    /* Close */
    if(closeBtn){
        closeBtn.addEventListener("click", function(){
            container.classList.remove("form-open");
            if(form){
                form.reset();
            }
            if(idInput){
                idInput.value = "";
            }
            lignes.forEach(l => l.classList.remove("active"));
            if(submitBtn){
                submitBtn.innerHTML = "<span class='icon'> Ajouter </span>"
            }
        });
    }
});
console.log("JS OK");