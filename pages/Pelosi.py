#!/usr/bin/env python3

import streamlit as st
import pandas as pd
from common import get_portfolio_data

name = "Pelosi"
st.set_page_config(page_title=f"{name} Portfolio", page_icon="📈")
st.sidebar.header(f"{name} Portfolio")

percentages = {'NVDA':17.11, 'GOOGL':15.08, 'PANW':10.46, 'AMZN':10.28, 'VST':9.83, 'AVGO':9.12, 'TEM':8.07, 'CRWD':5.50, 'AAPL':5.15, 'MSFT':4.81, 'TSLA':4.56}
start_date = '2025-01-28'
investment = 2000
reversed_df = get_portfolio_data(percentages, start_date, investment)

st.markdown(
	f"""
	### {name} stock portfolio
	Heralded as the queen of political stock trading, she made a name for herself by profiting in tech stocks that happened to benefit from legislation. Specializes in making \"notable, eyebrow raising\" trades.
	Insider trader emeritae...
"""
)

df = pd.DataFrame(list(percentages.items()), columns=['Ticker', 'Percentage'])
df.set_index('Ticker', inplace=True)
df['Percentage'] = df['Percentage'].round(2)

st.write("### Portfolio composition")
st.write(df)

col1, col2 = st.columns(2)

col1.subheader("Daily values")
col1.dataframe(reversed_df)

col2.subheader("Performance")
col2.markdown(f"""
			- Start value: ${investment:,.2f}
			- Start date: {start_date}
			- Current value: ${reversed_df.iloc[0]:,.2f}
			- Performance: {round((reversed_df.iloc[0]-investment)/investment*100, 2)}%
			"""
)

st.line_chart(reversed_df.iloc[::-1])