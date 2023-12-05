document.addEventListener('DOMContentLoaded', function() {
    const verCategoriasBtn = document.getElementById('ver-todas-categorias');
    const categoriasEscondidas = document.querySelectorAll('.hidden-categoria');
    const flechaCategorias = document.querySelector('.flecha-categorias');

    let flechaRotada = false;

    function mostrarCategorias() {
        categoriasEscondidas.forEach(function (item) {
            if (item.style.display === 'none' || item.style.display === '') {
                item.style.display = 'block';
                setTimeout(() => {
                    item.style.opacity = '1';
                    item.style.pointerEvents = 'auto';
                    item.style.transform = 'translateY(0)';
                }, 10);
            } else {
                item.style.opacity = '0';
                item.style.pointerEvents = 'none';
                item.style.transform = 'translateY(-100%)';
                setTimeout(() => {
                    item.style.display = 'none';
                }, 300);
            }
        });

        flechaRotada = !flechaRotada; // Cambiar el estado de la rotación
        flechaCategorias.style.transform = flechaRotada ? 'rotate(-180deg)' : 'rotate(0deg)';
    }

    verCategoriasBtn.addEventListener('click', mostrarCategorias);
});
