
async function pegarDados(){
    const response = await fetch('http://127.0.0.1:8000/');
    if(response === 200){
        const obj = await response.json();
    }
}