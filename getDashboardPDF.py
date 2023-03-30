import requests
import json
import os
from dotenv import load_dotenv
from datetime import date
import smtplib

load_dotenv()

def dashboard_filename():
    file_name = "dashboard-"+str(date.today())+".pdf"

    return file_name

def getDashboardPDF():

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

    with open(dashboard_filename(), 'wb') as f:
        f.write(response.content)
