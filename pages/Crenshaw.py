#!/usr/bin/env python3

import streamlit as st
import pandas as pd
from common import get_portfolio_data

name = "Crenshaw"
st.set_page_config(page_title=f"{name} Portfolio", page_icon="📈")
st.sidebar.header(f"{name} Portfolio")

percentages = {'META':32.00, 'FAS':14.00, 'AMZN':14.00, 'GOOGL':11.00, 'SPY':9.00, 'AAPL':7.00, 'USO':7.00, 'WYNN':6.00}
start_date = '2025-01-28'
investment = 2000
reversed_df = get_portfolio_data(percentages, start_date, investment)

st.markdown(
	f"""
	### {name} stock portfolio
	Daniel Reed Crenshaw[1] (born March 14, 1984)[2] is an American politician and former United States Navy SEAL officer serving as the U.S. representative for Texas's 2nd congressional district since 2019. He is a member of the Republican Party. In March 2021, The Daily Beast reported that Crenshaw had violated the Stop Trading on Congressional Knowledge (STOCK) Act of 2012, a federal transparency and conflict-of-interest law, by failing to properly disclose stock trades that he made in March 2020.
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