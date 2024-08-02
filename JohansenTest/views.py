# importing the render to display the response 
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#importing the relevant libraries for johansen test
import numpy as np
import pandas as pd
import yfinance as yf
import requests
from statsmodels.tsa.vector_ar.vecm import coint_johansen

# defining a view function which is triggered once appropriate url is entered
def JohansenTest(request) : 

    url = "https://financialmodelingprep.com/api/v3/stock-screener?sector=&apikey=pvDMXekTNwD8iPfQ9K8aCnLuXyvAUvYT"
    response = requests.get(url)
    if response.status_code == 200:
        stock_data = response.json()
        symbols = [company['symbol'] for company in stock_data]
    else:
        print(f"Error. Status code: {response.status_code}")
    
    stock_pairs=[]
    for j in range(len(symbols)):
        for k in range(j+1,len(symbols)):
            pair = (symbols[j] ,symbols[k])
            stock_pairs.append(pair)
    
    print(stock_pairs)

    # range of dates where we are comparing for cointegration
    start_date = '2010-01-01'
    end_date = '2022-10-16'

    # downloading the data from yfinance library for each pair in 
    data = yf.download([pair[0] for pair in stock_pairs] + [pair[1] for pair in stock_pairs], start = start_date, end = end_date)['Adj Close']

    # performing johansen test for each pair using statsmodels builtin function
    # parameters expressed briefly in documentation : https://www.statsmodels.org/dev/generated/statsmodels.tsa.vector_ar.vecm.coint_johansen.html#statsmodels.tsa.vector_ar.vecm.coint_johansen-returns
    coint_test_result_pair = coint_johansen(data, det_order = 0, k_ar_diff = 1)

    # Extracting eigen values and critical values, these are objects with each index 
    # representing the corresponding pair at that index in stock_pair 
    tracevalues = coint_test_result_pair.lr1
    criticalvalues = coint_test_result_pair.cvt

    # initialising an array with dictionary as its contents to hold information 
    # about individual pairs of stocks
    stock_dict = []

    # iterating thru the stock_pairs and interpreting results
    for i, (stock1, stock2) in enumerate(stock_pairs) : 
        stock_dict.append({
            'stock1' : stock1,
            'stock2' : stock2,
            'trace_stat' : tracevalues[i],
            'critical_stat' : criticalvalues[i],
            # key to indicate if stocks are cointegrated
            'cointegrated' : False,
        })
        # if tracevalue for that pair passes all critical values, they are cointegrated
        if(tracevalues[i] > criticalvalues[: -1]).all() :
            stock_dict[i]['cointegrated'] = True

    # displaying
    template = loader.get_template('JohansenTest/JohansenTest.html')

    # making variable accessible in the template
    context = {
        'stock_dict' : stock_dict,
    }

    #returning the response to webpage
    return HttpResponse(template.render(context, request))

    




