# Anime Productivity App

## Visão Geral
O Anime Productivity App é uma aplicação desktop desenvolvida em Python, com um tema de anime, que integra métodos de produtividade, como o Pomodoro, e permite a sincronização de tarefas com o Google Calendar. A aplicação possui uma interface gráfica moderna e personalizável, suporte a múltiplos usuários, e gera relatórios em PDF com elementos de anime.

## Tecnologias Utilizadas
- **Linguagem**: Python 3.10+
- **Interface Gráfica**: PyQt5 ou CustomTkinter
- **Banco de Dados**: SQLite (padrão) ou MySQL (configurável)
- **APIs**: Google Calendar (via google-api-python-client)
- **Notificações**: plyer
- **Geração de PDF**: ReportLab ou PyFPDF
- **Empacotamento**: PyInstaller

## Instalação
Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Uso
1. Execute o arquivo `main.py` para iniciar a aplicação.
2. Na tela de login, insira suas credenciais para acessar o sistema.
3. Utilize o dashboard para visualizar suas tarefas e iniciar sessões de Pomodoro.
4. Acesse as configurações para personalizar o tema e as notificações.

## Configuração de APIs
Para utilizar a integração com o Google Calendar, você precisará obter as chaves de API. Siga os passos abaixo:
1. Acesse o [Google Cloud Console](https://console.cloud.google.com/).
2. Crie um novo projeto e ative a API do Google Calendar.
3. Crie credenciais do tipo "OAuth 2.0 Client ID" e baixe o arquivo JSON.
4. Coloque o arquivo JSON na pasta do projeto e configure o caminho no código.

## Estrutura do Projeto
```
anime-productivity-app
├── gui
│   ├── __init__.py
│   ├── main_window.py
│   ├── login.py
│   ├── dashboard.py
│   └── settings.py
├── database
│   ├── __init__.py
│   ├── connection.py
│   └── schema.sql
├── api
│   ├── __init__.py
│   └── google_calendar.py
├── utils
│   ├── __init__.py
│   ├── authentication.py
│   ├── notifications.py
│   └── pdf_generator.py
├── tests
│   └── test_app.py
├── requirements.txt
├── main.py
├── AnimeProductivity.spec
└── README.md
```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.