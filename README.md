# Projeto de Álbum de Fotos

Este projeto consiste em uma aplicação web para seleção e gestão de álbuns de fotos. Ele é dividido em duas partes:
- **Backend**: API desenvolvida em Django.
- **Frontend**: Interface construída com HTML, CSS e JavaScript, rodando via extensão Live Server.

## 🚀 Tecnologias Utilizadas
- **Backend**: Django, Django REST Framework, PostgreSQL (ou outro banco configurado)
- **Frontend**: HTML, CSS, JavaScript
- **Ferramentas Adicionais**: Live Server (para rodar o frontend), dotenv (para gerenciamento de variáveis de ambiente)

---

## 🛠️ Configuração do Backend

1. Acesse a pasta do backend:
   ```sh
   cd Back
   ```
2. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.sample` e renomeie para `.env`.
   - Preencha as informações necessárias, como banco de dados e credenciais.
5. Realize as migrações do banco:
   ```sh
   python manage.py migrate
   ```
6. Crie um superusuário (opcional, para acesso ao admin):
   ```sh
   python manage.py createsuperuser
   ```
7. Inicie o servidor Django:
   ```sh
   python manage.py runserver
   ```

O backend estará disponível em `http://127.0.0.1:8000/`.

---

## 🌐 Configuração do Frontend

1. Acesse a pasta do frontend:
   ```sh
   cd Front
   ```
2. Abra o arquivo `login.html` no navegador ou utilize a extensão **Live Server** no VS Code para rodá-lo.
3. O frontend consumirá a API Django para interagir com os dados do álbum de fotos.

---

## 📌 Estrutura do Projeto
```
projeto-album/
│-- Back/               # Backend Django
│   ├── manage.py
│   ├── .env.sample     # Exemplo de variáveis de ambiente
│   ├── requirements.txt
│   └── ...
│
│-- Front/              # Frontend HTML, CSS, JS
│   ├── inicio.html
│   └── ...
│
│-- README.md           # Documentação
```

---

## 📝 Considerações
Caso tenha dúvidas ou problemas, verifique se todas as dependências estão instaladas corretamente e se as variáveis de ambiente estão configuradas. Para mais informações, consulte a documentação do Django e da API utilizada no frontend.

