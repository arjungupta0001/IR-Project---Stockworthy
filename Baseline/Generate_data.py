import requests
import csv
key = '581d249c75cc4a8ea6b89f675dd6dbc0'
tickers = {"MMM": "3M Company",
    "AXP": "American Express",
    "AMGN": "Amgen",
    "AAPL": "Apple Inc",
    "BA": "Boeing",
    "CAT": "Caterpillar Inc",
    "CVX": "Chevron",
    "CSCO": "Cisco",
    "KO": "The Coca-Cola Company",
    "DOW": "Dow Inc",
    "GS": "Goldman Sachs",
    "HD": "The Home Depot",
    "HON": "Honeywell",
    "IBM": "IBM",
    "INTC": "Intel",
    "JNJ": "Johnson & Johnson",
    "JPM": "JPMorgan Chase",
    "MCD": "McDonald's Corp",
    "MRK": "Merck & Co. Inc",
    "MSFT": "Microsoft",
    "NKE": "Nike",
    "PG": "Procter & Gamble",
    "CRM": "Salesforce",
    "TRV": "The Travelers Companies Inc",
    "UNH": "UnitedHealth Group Inc",
    "VZ": "Verizon",
    "V": "Visa Inc",
    "WMT": "Walmart",
    "DIS": "Walt Disney",
    "WBA": "Walgreens Boots"}

def add_entry_to_csv(filename, entry):
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['sno', 'headline', 'description', 'content', 'url', 'author', 'date', 'ticker']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow(entry)

for ticker in tickers.keys():
    q = tickers[ticker]
    fromdate = '2024-02-08' # yyyy-mm-dd
    todate = '2024-03-06' # yyyy-mm-dd
    response = requests.get('https://newsapi.org/v2/everything?q='+q+'&from='+fromdate+'&to='+todate+'&language=en&sortBy=popularity&apiKey='+key)
    x = response.json()
    for i in range (len(x['articles'])):
        entry = {
            'sno': i,
            'headline': x['articles'][i]['title'],
            'description': x['articles'][i]['description'],
            'content': x['articles'][i]['content'],
            'url': x['articles'][i]['url'],
            'author': x['articles'][i]['author'],
            'date': x['articles'][i]['publishedAt'],
            'ticker': ticker
        }
        add_entry_to_csv('data.csv', entry)