(function () {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {

        btn.addEventListener("click", (e) => {
            const confirmacion = confirm('¿Estas seguro de eliminar este registro?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
})();

(function () {
    const btnSuccess = document.querySelectorAll(".btnSuccess");

    btnSuccess.forEach(btn => {

        btn.addEventListener("click", (e) => {
            const confirmacion = confirm('¿Estas seguro de Guardar este registro?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
})();




