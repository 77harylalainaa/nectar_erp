document.addEventListener("DOMContentLoaded", function () {

    const restoreBtns = document.querySelectorAll(".btn-restore");

    restoreBtns.forEach(restoreBtn => {
        restoreBtn.addEventListener("click", function () {

            const id = this.dataset.id;
            const type = this.dataset.type;

            if (!confirm("Restaurer cet élément ?")) return;

            fetch("/archives/restore/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken()
                },
                body: JSON.stringify({
                    id: id,
                    type: type
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // supp la ligne du tableau
                    this.closest("tr").remove();
                } else {
                    console.log(data.error);
                    console.log("ID:", id, "TYPE:", type);
                    alert("Erreur lors de la restoration");
                }
            });
        });
    });
});

function getCSRFToken() {
    let cookieValue = null;
    const name = "csrftoken";

    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");

        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}