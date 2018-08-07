from cachetools.func import ttl_cache
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random


def get_gspread_client(access_key=None):
    if not access_key:
        access_key = 'secret.json'
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(access_key, scope)
    return gspread.authorize(creds)


@ttl_cache(maxsize=1, ttl=300)
def get_thesis_values(client=None):
    if not client:
        client = get_gspread_client()
    sheet = client.open('Table - Reseach Paper Topics')
    worksheet = sheet.worksheet('Raw Data')
    return [worksheet.col_values(i) for i in range(1, worksheet.col_count + 1)]


def get_thesis_topic():
    values = get_thesis_values()
    choices = [random.choice(x) for x in values]
    # Idea: maybe move this into the index.html template?
    return f'{choices[0]}: {choices[1]} {choices[2]} & {choices[3]} {choices[4]}'
