async function getUserInfo() {
    try {
        // Obtém o token do localStorage
        const token = localStorage.getItem('token');
        if (!token) {
            console.error('Token não encontrado!');
            return;
        }

        // Obtém o ID do usuário do localStorage (verifique se está salvo corretamente)
        const idUser = localStorage.getItem('user');
        if (!idUser) {
            console.error('ID do usuário não encontrado!');
            return;
        }

        // console.log("Token armazenado:", token);
        // console.log("ID do usuário:", idUser);

        // Faz a requisição para obter os dados do usuário
        const response = await fetch(`http://127.0.0.1:8000/api/users/${idUser}/`, {
            method: 'GET',
            headers: {
                'Authorization': `Token ${token}`,  // Adicionando "Token " antes do valor
                'Accept': 'application/json'
            },
        });

        // Verifica se a resposta foi bem-sucedida
        if (!response.ok) {
            throw new Error(`Erro ${response.status}: ${response.statusText}`); 
        }

        // Converte a resposta para JSON
        const data = await response.json();
        console.log('Informações do usuário:', data);

        return data;  // Retorna os dados do usuário

    } catch (error) {
        console.error('Erro ao buscar informações do usuário:', error);
    }
}

// Exemplo de uso:
getUserInfo().then(data => {
    if (data) {
        console.log('Nome do usuário:', data.name_photographer);
        document.getElementById('usuario').innerHTML = data.name_photographer;
    }
});
