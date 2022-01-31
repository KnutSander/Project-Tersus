# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:33:40 2021

@author: Arif

Current Inputs,
Sickday CSV.
Just date/Amount of people sick on that day.



"""

import pandas as pd

def ConvergeCalc1(row):
    Diff = row['90ma'] - row['5ma']
    return Diff
    
def ConvergeCalc2(row):
    Diff = row['29ema'] - row['5ema']
    return Diff


def AnalyseSickDays(CSV_File):

    df1 = pd.read_csv(CSV_File, parse_dates=True,index_col=1)
    df1 = df1.drop('Unnamed: 0', axis=1)
    df1['5ma'] = df1['SickCount'].rolling(window=5).mean()
    df1['10ma'] = df1['SickCount'].rolling(window=10).mean()
    df1['30ma'] = df1['SickCount'].rolling(window=30).mean()
    df1['60ma'] = df1['SickCount'].rolling(window=60).mean()
    df1['90ma'] = df1['SickCount'].rolling(window=90).mean()

    df1['29ema'] = df1['SickCount'].ewm(span=29,adjust=False).mean()
    df1['5ema'] = df1['SickCount'].ewm(span=5,adjust=False).mean()
    df1['MADiff'] = df1.apply (lambda row: ConvergeCalc1(row), axis=1)
    df1['EMADiff'] = df1.apply (lambda row: ConvergeCalc2(row), axis=1)
    dfDiff = df1.drop(columns=['5ma','10ma','30ma','60ma','90ma','29ema','5ema'])
    return dfDiff.dropna(axis=0,how='any')    
    




def NeuralSignalMA():
    df1 = AnalyseSickDays("Sickinfo.csv")

    check = False;

    df1 = df1.tail(7)
    for row in df1.iterrows():
        MA = row[1].values[1]
        if(MA < 0):
            check = True
        else:
            check = False
    return check

        
def NeuralSignalEMA():
    df1 = AnalyseSickDays("Sickinfo.csv")
    check = False;

    df1 = df1.tail(7)
    for row in df1.iterrows():
        EMA = row[1].values[2]
        if(EMA < 0):
            check = True
        else:
            check = False
    
    return check


def NeuralSignalRiskGradient():
    df1 = AnalyseSickDays("Sickinfo.csv")
    check = False;
    
    df1 = df1.tail(30)
    n1 = df1.iloc[0].values[1]
    n2 = df1.iloc[4].values[1]
    n3 = df1.iloc[24].values[1]
    n4 = df1.iloc[29].values[1]

    OldGrad = (n1 - n2) / 5
    NewGrad = (n3 - n4) /5
    
    if(OldGrad < NewGrad):
        check = True
    
    
    
    return check
    
    
    
