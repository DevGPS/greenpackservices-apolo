const $form_create_cereza =document.getElementById('form_create_cereza');
const $Lote = document.getElementById('Lote');

(function (){
    $form_create_cereza.addEventListener('submit',function (e) {
        let nombre =string($Lote.value).trim();
        if (nombre.length === 0) {
            alert('no puede estar vacio..');
            e.preventDefault();
        }
    });
})();