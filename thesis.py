from cachetools.func import ttl_cache
import gspread
import gspread_asyncio
from oauth2client.service_account import ServiceAccountCredentials
import random
import asyncio

def get_service_account_creds(access_key=None):
    if not access_key:
        access_key = 'secret.json'
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(access_key, scope)
    return creds


async def get_gspread_client(access_key=None):
    agcm = gspread_asyncio.AsyncioGspreadClientManager(get_service_account_creds)
    agc = await agcm.authorize()
    return agc


async def get_thesis_values(client=None):
    if not client:
        client = await get_gspread_client()
    sheet = await client.open('Table - Reseach Paper Topics')
    worksheet = await sheet.worksheet('Raw Data')
    return [await worksheet.col_values(i) for i in range(1, worksheet.col_count + 1)]


cached_values = None


async def get_thesis_topic():
    global cached_values
    if not cached_values:
        cached_values = await get_thesis_values()
    choices = [random.choice(x) for x in cached_values]
    # Idea: maybe move this into the index.html template?
    return f'{choices[0]}: {choices[1]} {choices[2]} & {choices[3]} {choices[4]}'


FETCH_PERIOD_SEC = 10


async def fetch_loop():
    global cached_values
    while True:
        print("Updating values")
        cached_values = await get_thesis_values()
        await asyncio.sleep(FETCH_PERIOD_SEC)

