#!/usr/bin/env python3

import streamlit as st
import pandas as pd
from common import get_portfolio_data

name = "Ackman"
st.set_page_config(page_title=f"{name} Portfolio", page_icon="📈")
st.sidebar.header(f"{name} Portfolio")

percentages = {'HHH':20.00, 'BN':15.00, 'QSR':11.00, 'NKE':11.00, 'HLT':10.00, 'CMG':10.00, 'GOOG':9.00, 'CP':8.00, 'GOOGL':5.00, 'SEG':1.00}
start_date = '2025-01-28'
investment = 2000
reversed_df = get_portfolio_data(percentages, start_date, investment)

st.markdown(
	f"""
	### {name} stock portfolio
	High-conviction investments in underperforming companies
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