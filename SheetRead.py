# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:22:38 2020

@author: Deepan
"""
import pandas as pd
import gspread
from apiclient.discovery import build
from google.oauth2.service_account import Credentials
import json
print("Google Sheet Data Fetch Start")
SCOPES = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_file("D:\\GoogleSheet\\Acth\\cred.json", scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)
client = gspread.authorize(credentials)
sheet = client.open("Test_Py").worksheet('TestSheet')  # Open the spreadhseet
data = sheet.get_all_records()  # Get a list of all records
sheetdf = pd.DataFrame(data)

print(sheetdf)



