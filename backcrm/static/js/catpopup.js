const openBtn = document.getElementById("open-categorie");
const popup = document.getElementById("popup-categorie");
const closeBtn = document.getElementById("close-popup");

if(openBtn){
    openBtn.addEventListener("click", () => {
        popup.style.display = "block";
    });
}

if(closeBtn){
    closeBtn.addEventListener("click", () => {
        popup.style.display = "none";
    });
}