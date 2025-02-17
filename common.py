#!/usr/bin/env python3

import pandas as pd
import yfinance as yf

def get_portfolio_data(percentages, start_date, investment):
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

    return reversed_df