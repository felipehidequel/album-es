// const username = document.getElementById('usuario');

// fetch('http://127.0.0.1:8000/api/users/${idUser}/')
// console.log(idUser);
// let idUser = localStorage.getItem('user')

// async function getUserInfo() {
//     try {
//         const token = localStorage.getItem('token');  // Obtém o token do localStorage

//         if (!token) {
//             console.error('Token não encontrado!');
//             return;
//         }

//         const response = await fetch('http://127.0.0.1:8000/api/users/${idUser}/', {
//             method: 'GET',
//             headers: {
//                 'Authorization': `Bearer ${token}`,  // Passa o token no cabeçalho Authorization
//                 'Accept': 'application/json',  // Define que esperamos resposta em JSON
//             },
//         });

//         if (!response.ok) {
//             throw new Error('Erro ao buscar informações do usuário');
//         }

//         const data = await response.json();
//         console.log('Informações do usuário:', data);
//         return data;  // Aqui você pode acessar os dados, como o nome do usuário
//     } catch (error) {
//         console.error('Erro ao buscar informações do usuário:', error);
//     }
// }

// // Exemplo de uso:
// getUserInfo().then(data => {
//     if (data) {
//         console.log('Nome do usuário:', data.name_photographer);
//     }
// });
async function getUserInfo() {
    try {
        const token = localStorage.getItem('token');  // Obtém o token do localStorage

        if (!token) {
            console.error('Token não encontrado!');
            return;
        }

        const idUser = localStorage.getItem('user');  // Substitua pelo ID correto do usuário ou use o ID do usuário autenticado

        const response = await fetch(`http://127.0.0.1:8000/api/users/${idUser}/`, {  // Corrija a URL aqui
            method: 'GET',
            headers: {
                'Authorization': `${token}`,  // Passa o token no cabeçalho Authorization
                'Accept': 'application/json',  // Define que esperamos resposta em JSON
            },
        });

        if (!response.ok) {
            throw new Error('Erro ao buscar informações do usuário');
        }

        const data = await response.json();
        console.log('Informações do usuário:', data);
        return data;  // Aqui você pode acessar os dados, como o nome do usuário
    } catch (error) {
        console.error('Erro ao buscar informações do usuário:', error);
    }
}

// Exemplo de uso:
getUserInfo().then(data => {
    if (data) {
        console.log('Nome do usuário:', data.name_photographer,);
    }
});
