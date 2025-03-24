
document.querySelector('form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const username = document.getElementById('inpt-usuario').value;
    const password = document.getElementById('inpt-senha').value;

    try {
        const csrftoken = getCsrfToken(); // Obtém o token CSRF

        const response = await fetch('http://127.0.0.1:8000/api/users/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN': csrftoken,
                'Accept': 'application/json'
            },
            body: JSON.stringify({ username, password }),
            credentials: 'include' // Necessário para cookies
        });

        if (!response.ok) {
            throw new Error(`Erro: ${response.status} - ${response.statusText}`);
        }

        const data = await response.json();

        if (data.status) {
            localStorage.setItem('token', data.token);
            alert('Login bem-sucedido!');
            window.location.href = 'Inicio.html';
        } else {
            alert('Usuário ou senha incorretos!');
        }
    } catch (error) {
        console.error('Erro no login:', error);
        alert('Erro ao tentar fazer login. Verifique o console.');
    }
});

function getCsrfToken() {
    const name = 'csrftoken=';
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name)) {
            return cookie.substring(name.length);
        }
    }
    return '';
}
