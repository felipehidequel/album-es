
 async function criarAlbum() {
    // evt.preventDefault();
    const nomeAlbum = document.getElementById('album-nome').value;
    const iptAlbum = document.getElementById('ipt-album').value;
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
        
        // Faz a requisição para obter os dados do usuário
        // debugger;
        // const response = await fetch("http://127.0.0.1:8000/api/gallery/album/", {
        //     method: 'POST',
        //     headers: {
        //         // 'Authorization': `Token ${token}`,  // Adicionando "Token " antes do valor
        //         "Accept": "application/json",
        //         "Content-Type": "application/json"
        //     },
        //     body: JSON.stringify({
        //         name_album: nomeAlbum,
        //         photographer: Number(idUser)
        //     }),
        // }).then(response => response.json())
        // .then(data => {alert(data)})
        // .catch(error => {console.error("error", error.stack)});
        // fetch("http://127.0.0.1:8000/api/gallery/album/", {
        //     method: "POST",
        //     headers: {
        //         "Accept": "application/json",
        //         "Content-Type": "application/json"
        //     },
        //     body: JSON.stringify({
        //         name_album: nomeAlbum,
        //         photographer: Number(idUser)
        //     }),
        // })
        // .then(response => {
        //         if (!response.ok) {
        //             return response.text().then(err => {
        //                 alert(`Erro HTTP ${response.status}: ${err}`);
        //             });
        //         }
        //         alert(response.json());
        //     })
        //     .then(data => {
        //         // alert("Sucesso: " + data);
                
        //     })
        //     .catch(error => {
        //         console.error("Erro na requisição:", error);
        //         console.error("Stack trace:", error.stack);
        //     });
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
            alert("Sucesso: " + JSON.stringify(data)); // Agora os dados são exibidos corretamente
        })
        .catch(error => {
            console.error("Erro na requisição:", error);
            console.error("Stack trace:", error.stack);
        });
        alert("aqui");
        // Verifica se a resposta foi bem-sucedida
        // if (!response.ok) {
        //     console.log("response");
        //     throw new Error(`Erro ${response.status}: ${response.statusText}`); 
        // }
        
        // Converte a resposta para JSON
        // const data = await response.json();
        // console.log('Informações do usuário:', data);
        // Retorna os dados do usuário
        
        
    } catch (error) {
        // console.error('Erro ao buscar informações do usuário:', error);
        alert("dt");
    }
}


// async function postAlbum() {
//     const nomeAlbum = document.getElementById('album-nome').value;
//     console.log("Nome do álbum:", nomeAlbum);

//     if (!nomeAlbum.trim()) {
//         alert('O nome do álbum não pode ser vazio!');
//         return;
//     }

//     try {
//         // Obtém o token do localStorage
//         const token = localStorage.getItem('token');
//         if (!token) {
//             console.error('Token não encontrado!');
//             return;
//         }

//         // Obtém o ID do usuário do localStorage
//         const idUser = localStorage.getItem('user');
//         if (!idUser) {
//             console.error('ID do usuário não encontrado!');
//             return;
//         }

//         console.log("ID do usuário:", idUser);

//         // Faz a requisição para criar o álbum
//         const response = await fetch('http://127.0.0.1:8000/api/gallery/album/', {
//             method: 'POST',
//             headers: {
//                 'Authorization': `Token ${token}`, // Corrigido
//                 'Accept': 'application/json',
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({
//                 "name_album": nomeAlbum,
//                 "photographer": idUser
//             }),
//         });

//         if (!response.ok) {
//             throw new Error(`Erro ${response.status}: ${response.statusText}`);
//         }

//         // Converte a resposta para JSON
//         const data = await response.json();
//         console.log('Álbum criado com sucesso:', data);

//         // Exibir mensagem de sucesso
//         alert('Álbum criado com sucesso!');

//         return data;  

//     } catch (error) {
//         console.error('Erro ao criar álbum:', error);
//         alert('Erro ao criar álbum!');
//     }
// }