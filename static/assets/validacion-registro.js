document.addEventListener('DOMContentLoaded', function () {
    const formRegistro = document.querySelector('.js-loginFormModal');

    formRegistro.addEventListener('submit', function (event) {
        // Resetear mensajes de error
        const errorMessages = document.querySelectorAll('.error-text-modal');
        errorMessages.forEach(function (errorMessage) {
            errorMessage.textContent = '';
        });

        // Validar campos
        const username = document.getElementById('username-modal').value;
        const nombre = document.getElementById('nombre-modal').value;
        const apellido = document.getElementById('apellido-modal').value;
        const nacimiento = document.getElementById('nacimiento-modal').value;
        const genero = document.getElementById('genero-modal').value;
        const password = document.getElementById('password-modal').value;
        const confirmPassword = document.getElementById('password-confirmn').value;

        if (username.trim() === '') {
            showError('username-modal', 'Ingresa tu email');
        }

        if (nombre.trim() === '') {
            showError('nombre-modal', 'Ingresa tu nombre');
        }

        if (apellido.trim() === '') {
            showError('apellido-modal', 'Ingresa tu apellido');
        }

        if (nacimiento.trim() === '') {
            showError('nacimiento-modal', 'Ingresa tu año de nacimiento');
        }

        if (genero.trim() === '') {
            showError('genero-modal', 'Ingresa tu género');
        }

        if (password.trim() === '') {
            showError('password-modal', 'Ingresa tu contraseña');
        } else if (password.length < 6) {
            showError('password-modal', 'La contraseña debe tener al menos 6 caracteres');
        }

        if (confirmPassword.trim() === '') {
            showError('password-confirmn', 'Confirma tu contraseña');
        } else if (confirmPassword.length < 6 || confirmPassword !== password) {
            showError('password-confirmn', 'Las contraseñas no coinciden');
        }

        // Evitar que el formulario se envíe si hay errores
        if (document.querySelectorAll('.error-text-modal:empty').length === 7) {
            // Aquí puedes agregar cualquier lógica adicional antes de enviar el formulario
            alert('Formulario válido. Puedes agregar tu lógica de envío aquí.');
        } else {
            event.preventDefault();
        }
    });

    function showError(inputId, message) {
        var errorMessage = document.querySelector('#' + inputId + ' + .error-text-modal');
        errorMessage.textContent = message;
    }
});
