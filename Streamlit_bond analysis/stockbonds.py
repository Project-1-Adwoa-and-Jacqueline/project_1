import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from pathlib import Path
import plotly.graph_objects as go

#Read and access individual stocks in S&P500
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sp_table = pd.read_html(url)
sp_tickers = sp_table[0]['Symbol'].to_list()

tickers = st.multiselect("Select your stocks",sp_tickers)

if not tickers:
    st.error("Please select at least one ticker.")
else:
    periods = ['1mo', '6mo', '1y','2y','3y']
    period = st.sidebar.selectbox('Period', periods, index=2)
    figs = {}



    total_so_far = yf.Ticker(tickers[0]).history(interval='1d', period=period)['Close']
    
    for i in range(len(tickers)):
        hist = yf.Ticker(tickers[i]).history(interval='1d', period=period)
        total_so_far = total_so_far.add(hist['Close'])
        fig = go.Scatter(x=hist.index, y=hist['Close'], mode='lines', name=tickers[i])
        figs[tickers[i]] = fig

    tickerSymbol = st.sidebar.selectbox('Stock ticker', tickers)
    show_all = st.sidebar.checkbox('Show all?')
    fig = go.Figure()
    if show_all:
        total_fig = go.Scatter(
            x=total_so_far.index,
            y=total_so_far, mode='lines',
            name='Total Value'

        )
        fig.add_trace(total_fig)

        for ticker in figs:
            fig.add_trace(figs[ticker])
    else:
        fig.add_trace(figs[tickerSymbol])

    fig.update_layout(
        title="Closing Stock Price",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        legend_title="Stocks",
    )

    st.plotly_chart(fig, use_container_width=True)

    data = yf.Ticker(tickerSymbol).info

    #CSV Data for top 5 stocks
    top5 = yf.download(tickers,interval='1d',period=period)['Close']

    # Readimg S&P 500 from closing prices
    sp500_cs = Path("SP500_historical.csv")
    sp500_df = pd.read_csv(sp500_cs, index_col="Date", parse_dates=True)
    sp500_df.sort_index(inplace=True)
    # Rename `Close` Column to be specific to this portfolio.
    sp500_df.columns=["S&P500"]

    df_combined = pd.concat([top5, sp500_df], axis='columns')

    #Sharpe Ratio for relationship between bonds and S&P500
    # read ibond csv file
    ibonds_path= Path("ibonds_cleaned_data.csv")
    ibonds_df = pd.read_csv(ibonds_path)

   
    # annualize variable interest rate
    ibonds_df["annualized six-month variable interest rate"] = np.maximum((ibonds_df["six-month inflation rate"] * 2), 0)

    # combined rate
    ibonds_df["aggregate annualized interest rate"] = ibonds_df["annualized six-month variable interest rate"] + ibonds_df["fixed rate"]
    ibonds_df.head()

    #locate 2022 risk free rate to compare with stocks
    ibonds_df=ibonds_df[48:50]

   # drop fixed rate and six-month inflation rate to ease visualization
    new_ibondsdf= ibonds_df[ ['date','aggregate annualized interest rate'] ]
    new_ibondsdf.head().set_index('date', inplace=True)
    
    # plot_1 = sharpe.plot(kind='bar')
    # new_ibondsdf.plot(kind='bar')
    st.title("Ibonds Interest Rate")
    st.bar_chart(new_ibondsdf)

    #calculate mean of the annualized risk free rate
    rf_rate=ibonds_df['aggregate annualized interest rate'].mean()

    std_dev = df_combined.std()
    # Calculate the annualized standard deviation using 252 trading days
    annual_std = std_dev * np.sqrt(252)
    annualized_return=df_combined.mean()
    sharpe_ratio = (annualized_return - rf_rate) / annual_std
    sharpe_ratio.sort_values(ascending=False)
    #print(sharpe_ratio.sort_values(ascending=False))

    st.title("Sharpe Ratio For Stocks and S&P500 ")
    st.bar_chart(sharpe_ratio)






    





    