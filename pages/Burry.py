#!/usr/bin/env python3

import streamlit as st
import pandas as pd
from common import get_portfolio_data

st.set_page_config(page_title="Burry Portfolio", page_icon="📈")
st.sidebar.header("Burry Portfolio")

percentages = {'BABA':27.00, 'JD':23.00, 'FOUR':20.00, 'BIDU':13.00, 'MOH':9.00, 'REAL':4.00, 'OLPX':2.00, 'ACIC':1.00}
start_date = '2025-01-28'
investment = 2000

st.markdown(
	"""
	### Burry stock portfolio
	Michael James Burry is an American investor and hedge fund manager. He founded the hedge fund Scion Capital, which he ran from 2000 until 2008 before closing it to focus on his personal investments. He is best known for being among the first investors to predict and profit from the subprime mortgage crisis between 2007 and 2010.
"""
)

df = pd.DataFrame(list(percentages.items()), columns=['Ticker', 'Percentage'])
df.set_index('Ticker', inplace=True)
df['Percentage'] = df['Percentage'].round(2)

st.write("### Portfolio composition")
st.write(df)

st.write("### Portfolio Performance")
st.write(f"Start value: ${investment:,.2f} &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Start date: {start_date}")

reversed_df = get_portfolio_data(percentages, start_date, investment)
st.write(f"Current value: ${reversed_df.iloc[0]:,.2f} &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Performance: {round((reversed_df.iloc[0]-investment)/investment*100, 2)}%")

st.dataframe(reversed_df)
st.line_chart(reversed_df.iloc[::-1])