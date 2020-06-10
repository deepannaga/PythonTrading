# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:50:04 2020

@author: Deepan
"""

import time
import datetime
import sys
import pandas as pd
import os
import sqlite3
from alice_blue import *
from random import random

access_token = AliceBlue.login_and_get_access_token(username='######', password='######', twoFA='######',  api_secret='######')

alice = AliceBlue(username='######', password='######', access_token=access_token)

tickers = ["SUNPHARMA","CIPLA","NTPC","INFRATEL","INDUSINDBK","HEROMOTOCO","BAJFINANCE",
           "HCLTECH","DRREDDY","VEDL","SHREECEM","TITAN","TCS"] 

socket_opened = False

db = sqlite3.connect('D:/Python_Auto/Prac1/db/ticks.db')

def create_tables(tokens):
    c=db.cursor()
    for i in tokens:
        c.execute("CREATE TABLE IF NOT EXISTS TOKEN{} (ts datetime primary key,price real(15,5), volume integer)".format(i))
    try:
        db.commit()
    except:
        db.rollback()
        
def event_handler_quote_update(message):
    global ltp
    #print(f"quote update {message}")
    #print("Symbol= ",message["instrument"][2],"Time = ",message["exchange_time_stamp"],"Token = ",message["token"],"LTP = ",message["ltp"],"Volume = ",message["volume"])
    token =message["token"]
    print(token)
    create_tables(token)   
    
def open_callback():
    global socket_opened
    socket_opened = True

starttime=time.time()
timeout = time.time() + 60*60*1  # 60 seconds times 360 meaning 6 hrs

alice.start_websocket(subscribe_callback=event_handler_quote_update,
                      socket_open_callback=open_callback,
                      run_in_background=True)
while(socket_opened==False):
    pass
while time.time() <= timeout:
    for tick in tickers:
        try:
            alice.subscribe(alice.get_instrument_by_symbol('NSE', tick), LiveFeedType.COMPACT)
            time.sleep(10)
        except KeyboardInterrupt:
            print('\n\nKeyboard exception received. Exiting.')
            exit()   
