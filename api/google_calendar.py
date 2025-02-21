"""
Módulo para integração com a API do Google Calendar.
Utiliza google-api-python-client para autenticação e operações no calendário.
"""

import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime

# Definição dos escopos de acesso necessários para o Google Calendar.
SCOPES = ['https://www.googleapis.com/auth/calendar']

class GoogleCalendarAPI:
    def __init__(self, credentials_file='credentials.json', token_file='token.pickle'):
        """
        Inicializa a classe GoogleCalendarAPI.
        :param credentials_file: Caminho para o arquivo JSON com as credenciais do OAuth.
        :param token_file: Caminho para o arquivo de token salvo.
        """
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.creds = None
        self.service = None
        self.authenticate()

    def authenticate(self):
        """
        Realiza a autenticação do usuário com a API do Google Calendar.
        Primeiro tenta carregar um token salvo e, caso não exista ou esteja expirado,
        inicia o fluxo de autenticação.
        """
        # Verifica se o token já existe
        if os.path.exists(self.token_file):
            with open(self.token_file, 'rb') as token:
                self.creds = pickle.load(token)
        
        # Se não houver credenciais válidas, inicia o fluxo de login
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_file, SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Salva as credenciais para futuras execuções
            with open(self.token_file, 'wb') as token:
                pickle.dump(self.creds, token)
        
        # Constrói o serviço da API do Calendar
        self.service = build('calendar', 'v3', credentials=self.creds)

    def list_events(self, calendar_id='primary', max_results=10):
        """
        Lista os próximos eventos do calendário.
        :param calendar_id: ID do calendário (padrão: 'primary').
        :param max_results: Número máximo de eventos a serem retornados.
        :return: Lista de eventos.
        """
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indica UTC time
        events_result = self.service.events().list(
            calendarId=calendar_id, 
            timeMin=now,
            maxResults=max_results, 
            singleEvents=True, 
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])
        return events

    def add_event(self, event, calendar_id='primary'):
        """
        Adiciona um novo evento ao calendário.
        :param event: Dicionário com os dados do evento.
        :param calendar_id: ID do calendário (padrão: 'primary').
        :return: Evento criado.
        """
        created_event = self.service.events().insert(
            calendarId=calendar_id, 
            body=event
        ).execute()
        return created_event

# Função para criar um evento
def create_event_summary(title, description, start_time, end_time):
    event = {
        'summary': title,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'America/Sao_Paulo',
        },
    }
    return event