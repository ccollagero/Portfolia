#!/usr/bin/env python3

import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="Pelosi Portfolio", page_icon="📈")
st.sidebar.header("Pelosi Portfolio")

percentages = {'NVDA':17.11, 'GOOGL':15.08, 'PANW':10.46, 'AMZN':10.28, 'VST':9.83, 'AVGO':9.12, 'TEM':8.07, 'CRWD':5.50, 'AAPL':5.15, 'MSFT':4.81, 'TSLA':4.56}
start_date = '2025-01-28'
investment = 2000

st.markdown(
	"""
	### Pelosi stock portfolio
	Heralded as the queen of political stock trading, she made a name for herself by profiting in tech stocks that happened to benefit from legislation. Specializes in making \"notable, eyebrow raising\" trades.
	### Insider trader emeritae...
"""
)

st.write(f"Start value: ${investment:,.2f} &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Start date: {start_date}")

data = yf.download(list(percentages.keys()), start=start_date)
start = data['Close'].iloc[0]
index_list = start.index.tolist()

holdings = {}
for idx in index_list:
	inv = investment * percentages[idx] / 100
	shares = inv / start[idx]
	holdings[idx] = shares
	
holdings_series = pd.Series(holdings)

# Multiply each column by the corresponding holding and sum across columns to get daily portfolio value
portfolio_daily_value = data['Close'].mul(holdings_series, axis=1).sum(axis=1)
portfolio_daily_value.index = portfolio_daily_value.index.strftime('%Y-%m-%d')
portfolio_daily_value = portfolio_daily_value.rename('Portfolio Value ($$)')

reversed_df = portfolio_daily_value.iloc[::-1]
reversed_df = reversed_df.round(2)

st.write(f"Current value: ${reversed_df.iloc[0]:,.2f} &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Performance: {round((reversed_df.iloc[0]-investment)/investment*100, 2)}%")

st.dataframe(reversed_df)
st.line_chart(portfolio_daily_value)