import requests
import json
import os
from dotenv import load_dotenv
from datetime import date
import smtplib

load_dotenv()

api_key = os.environ.get('API_KEY')
graphql_url = 'https://api.newrelic.com/graphql'
headers = {
    'Content-Type': 'application/json',
    'API-Key': api_key
}

query = """
mutation {
  dashboardCreateSnapshotUrl(guid: "Mzc4NzcyM3xWSVp8REFTSEJPQVJEfDc0OTg4ODQ")
}
"""

response = requests.post(graphql_url, headers=headers, json={'query': query})

data = json.loads(response.text)
screenshot_url = data['data']['dashboardCreateSnapshotUrl']

response = requests.get(screenshot_url, headers=headers)

file_name = "dashboard-"+str(date.today())+".pdf"

with open(file_name, 'wb') as f:
    f.write(response.content)
