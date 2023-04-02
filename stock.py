import streamlit as st
import yfinance as yf
import pandas as pd
st.title('Finance Dashboard')
st.caption('Project by Maitreyee Mitra of CSE-AIML')
tickers=('TSLA','AAPL','SMSN.IL','MSFT','BTC-USD','ETH-USD','SBIN.NS','INDA')
dropdown = st.multiselect('Pick your assets',tickers)

start=st.date_input('Start',value=pd.to_datetime('2021-01-01'))
end=st.date_input('End',value=pd.to_datetime('today'))

def relativereturns(df):
    rel=df.pct_change()
    cumreturn=(1+rel).cumprod()-1
    cumreturn=cumreturn.fillna(0)
    return cumreturn

if len(dropdown) >0 :
    #df = yf.download(dropdown,start,end)['Adj Close']
    #now we apply relative returns
    df = relativereturns(yf.download(dropdown,start,end)['Adj Close'])
    st.line_chart(df)