import requests

# Base URL for the Frankfurter API
BASE_URL = 'https://api.frankfurter.app/'

# Endpoint for latest exchange rates
endpoint = 'latest'

# Parameters for the API request

# Make the request to the API
response_euro = requests.get(f'{BASE_URL}{endpoint}', params = {
    'base': 'EUR',
    'symbols': 'USD,GBP,JPY,CNY'
})

response_dollar = requests.get(f'{BASE_URL}{endpoint}', params = {
    'base': 'USD',
    'symbols': 'EUR,GBP,JPY,CNY'
})

response_livres = requests.get(f'{BASE_URL}{endpoint}', params = {
    'base': 'GBP',
    'symbols': 'EUR,USD,JPY,CNY'
})

response_yen = requests.get(f'{BASE_URL}{endpoint}', params = {
    'base': 'JPY',
    'symbols': 'EUR,GBP,USD,CNY'
})

response_yuan = requests.get(f'{BASE_URL}{endpoint}', params = {
    'base': 'CNY',
    'symbols': 'EUR,GBP,JPY,USD'
})


# Check if the request was successful (status code 200)
if response_yuan.status_code == 200:
    exchange_rates_euro = response_euro.json()['rates']
    exchange_rates_dollar = response_dollar.json()['rates']
    exchange_rates_livres = response_livres.json()['rates']
    exchange_rates_yen = response_yen.json()['rates']
    exchange_rates_yuan = response_yuan.json()['rates']
else:
    # Print an error message if the request failed
    print(f"Error: {response_yuan.status_code} - {response_yuan.reason}")