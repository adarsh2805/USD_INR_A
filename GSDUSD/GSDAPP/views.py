
from GSDAPP.models import GSDMODEL,INR
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from django.http import HttpResponse
from django.shortcuts import render


import json
import requests

def index(request):
    
    # #taking the data using csv
    df = pd.read_csv('C:\\new_project_2\\GSDUSD\\template\\USD.csv')
    records = df.to_records()
    print(records)
    for record in records:
            gsdmodel=GSDMODEL(Characteristic = record[1],
            GDP_in_billion = record[2])
    try:
        gsdmodel.save()
    except:
        print('duplicates values not allowed')
     
    # taking the value from API
    # response=requests.get('https://api.currencyfreaks.com/v2.0/rates/latest?apikey=0a0bbf757c3a42d1b8a811ee661a808c',timeout=30,verify=False)
    # print(response.json)

    #taking the data from data base
    qs = GSDMODEL.objects.all()
    projects_data = [
        {
            'Characteristic': x.Characteristic,
            'GDP_in_billion': x.GDP_in_billion
        } for x in qs
    ]
    x=[i['Characteristic'] for i in projects_data]
    y=[i['GDP_in_billion'] for i in projects_data]
    x_usd = json.dumps(x)
    x_srange = min(x)
    x_erange = max(x)

    y_srange = min(y)
    y_erange = max(y)

    y_usd= json.dumps(y)
    
    print(len(x),len(y))
    print(x,y)

    # taking the INR value from SQL
    price = INR.objects.all()
    price_value = [
        {
            'price': x.rupee,
        } for x in price
        ]
    pr=price_value[0]['price']
    y_ind=[int(i*pr) for i in y]
    ind_ysrange = min(y_ind)
    ind_yerange = max(y_ind)
    print(y_ind)
    context = {'x' : x_usd, 'y' : y_usd,'y_ind' : y_ind,'x_srange' : x_srange,'x_erange' : x_erange ,'y_srange' :y_srange,'y_erange' : y_erange,'ind_ysrange':ind_ysrange,'ind_esrange': ind_yerange}


    return render(request, "index.html", context=context)
