#!/usr/bin/env python3

import streamlit as st
import pandas as pd
from common import get_portfolio_data

name = "Goldman"
st.set_page_config(page_title=f"{name} Portfolio", page_icon="📈")
st.sidebar.header(f"{name} Portfolio")

percentages = {'TSLA':34.00, 'CRM':27.00, 'GOOGL':10.00, 'MSFT':7.00, 'NVS':6.00, 'JNJ':5.00, 'ARE':4.00, 'PEP':4.00, 'ADM':3.00}
start_date = '2025-01-28'
investment = 2000
reversed_df = get_portfolio_data(percentages, start_date, investment)

st.markdown(
	f"""
	### {name} stock portfolio
	Daniel Sachs Goldman (born February 26, 1976)[1][2] is an American attorney, politician, and heir; he is a member of the U.S. House of Representatives from New York's 10th congressional district. Goldman's financial disclosures indicate he has a line of credit from Goldman Sachs worth up to $50 million in addition to investments in weapons manufacturer Sturm, Ruger & Co., defense contractors Lockheed Martin and Northrop Grumman, oil companies Chevron, Exxon Mobil, and Halliburton, and Rupert Murdoch's Fox Corporation & News Corp.
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