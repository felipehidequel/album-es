
 async function criarAlbum() {
    // evt.preventDefault();
    const nomeAlbum = document.getElementById('album-nome').value;
    // const iptAlbum = document.getElementById('ipt-album').value;
    console.log("Nome:" + nomeAlbum);

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
        console.log("ID do usuário:", idUser);
        
        fetch("http://127.0.0.1:8000/api/gallery/album/", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name_album: nomeAlbum,
                photographer: Number(idUser)
            }),
        }).then(response => {
            if (!response.ok) {
                return response.text().then(err => {
                    alert(`Erro HTTP ${response.status}: ${err}`);
                    throw new Error(`Erro HTTP ${response.status}: ${err}`); // Interrompe a execução
                });
            }
            return response.json(); // Retorna a Promise que será resolvida no próximo .then()
        })
        .then(data => {
            alert("Sucesso: " + JSON.stringify(data));
             // Agora os dados são exibidos corretamente
            uploadPhoto(Number(data.id));
        })
        .catch(error => {
            console.error("Erro na requisição:", error);
            console.error("Stack trace:", error.stack);
        });
        alert("aqui");
        
    } catch (error) {
        // console.error('Erro ao buscar informações do usuário:', error);
        alert("dt");
    }
}

// document.getElementById('fileInput').addEventListener('change', function(event) {
//     const file = event.target.files[0];
//     if (file) {
//         document.getElementById('filePath').textContent = `Caminho do arquivo: ${file.name}`;
//     } else {
//         document.getElementById('filePath').textContent = 'Nenhum arquivo selecionado';
//     }
// });

// async function uploadPhoto(albumId) {
//     const inputFile = document.getElementById('ipt-album').files;
//     console.log("Input file:", inputFile[0]);
//     // console.log("Quantidade de arquivos selecionados:", inputFile.files.length);

//     alert(albumId);
//     debugger;
//     // if (!inputFile.files.length) {
//     //     alert('Por favor, selecione uma foto.');
//     //     return;
//     // }

//     // if (!inputFile || !inputFile.files.length) {
//     //     alert('Por favor, selecione uma foto antes de enviar.');
//     //     return;
//     // }

//     const file = inputFile[0];
//     const token = localStorage.getItem('token');

//     if (!token) {
//         console.error('Token não encontrado!');
//         return;
//     }

//     const formData = new FormData();
//     formData.append('album', albumId); // ID do álbum
//     formData.append('name_photo', file.name); // Nome da foto
//     formData.append('photo', file); // Arquivo da foto
//     console.log(file.path);
//     try {
//         const response = await fetch('http://127.0.0.1:8000/api/gallery/photo/', {
//             method: 'POST',
//             headers: {
//                 'Authorization': `Token ${token}`
//             },
//             body: formData // FormData para enviar arquivo
//         });

//         if (!response.ok) {
//             throw new Error(`Erro ${response.status}: ${response.statusText}`);
//         }

//         const data = await response.json();
//         console.log('Foto enviada com sucesso:', data);
//         alert('Foto enviada com sucesso!');

//     } catch (error) {
//         console.error('Erro ao enviar a foto:', error);
//         alert(`Erro ao enviar a foto. ${error.message}`);
//     }
// }
async function uploadPhoto(albumId) {
    const inputFile = document.getElementById('ipt-album'); // Pega o input
    if (!inputFile.files.length) {
        alert('Por favor, selecione uma foto.');
        return;
    }

    const file = inputFile.files[0]; // Pega o arquivo
    const token = localStorage.getItem('token'); // Obtém o token

    if (!token) {
        console.error('Token não encontrado!');
        return;
    }

    // Criando o FormData e adicionando os campos necessários
    const formData = new FormData();
    formData.append('album', albumId);      // ID do álbum (deve ser um número)
    formData.append('name_photo', file.name); // Nome do arquivo
    formData.append('photo', inputFile.files[0]);         // O próprio arquivo

    // console.log("FormData antes de enviar:", [...formData.entries()]);

    try {
        // Fazendo a requisição POST
        const response = await fetch('http://127.0.0.1:8000/api/gallery/photo/', {
            method: 'POST',
            headers: {
                'Authorization': `Token ${token}` // Apenas o token, sem definir Content-Type
            },
            body: formData // Enviando os dados
        });

        if (!response.ok) {
            const errorText = await response.text(); // Captura detalhes do erro
            throw new Error(`Erro ${response.status}: ${errorText}`);
        }

        const data = await response.json();
        console.log('Foto enviada com sucesso:', data);
        alert('Foto enviada com sucesso!');

    } catch (error) {
        console.error('Erro ao enviar a foto:', error);
        alert(`Erro ao enviar a foto: ${error.message}`);
    }
}
