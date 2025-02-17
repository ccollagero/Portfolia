#!/usr/bin/env python3

import streamlit as st
import pandas as pd
from common import get_portfolio_data

st.set_page_config(page_title="Rouzer Portfolio", page_icon="📈")
st.sidebar.header("Rouzer Portfolio")

percentages = {'JETS':15.00, 'NVDA':14.00, 'V':11.00, 'MA':11.00, 'GLD':11.00, 'BA':10.00, 'XLK':10.00, 'AMD':9.00, 'RTX':5.00, 'SPTM':5.00}
start_date = '2025-01-28'
investment = 2000
reversed_df = get_portfolio_data(percentages, start_date, investment)

st.markdown(
	"""
	### Rouzer stock portfolio
	David Cheston Rouzer is an American politician who is the U.S. representative for North Carolina's 7th congressional district. As a prolific public market investor, Rouzer posted a 149% portfolio gain for 2024, beating every other U.S. Congressman and more than doubling the gains posted by Nancy Pelosi.
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