from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime

# Função para autenticar e criar um serviço do Google Calendar
def authenticate_google_calendar(token_path='token.json', scopes=['https://www.googleapis.com/auth/calendar']):
    creds = None
    # O arquivo token.json armazena as credenciais de acesso do usuário
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, scopes)
    # Se não houver credenciais válidas, o usuário deve fazer login
    if not creds or not creds.valid:
        raise Exception("Credenciais inválidas ou não encontradas. Por favor, autentique-se novamente.")
    
    service = build('calendar', 'v3', credentials=creds)
    return service

# Função para adicionar um evento ao Google Calendar
def add_event_to_calendar(service, event):
    try:
        event_result = service.events().insert(calendarId='primary', body=event).execute()
        return event_result
    except Exception as e:
        print(f"Erro ao adicionar evento: {e}")
        return None

# Função para listar eventos do Google Calendar
def list_events(service, max_results=10):
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indica UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=max_results, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    return events

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