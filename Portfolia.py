#!/usr/bin/env python3

import streamlit as st

st.set_page_config(
	page_title="Portfolia",
	page_icon="👋",
)

details = {"money": 2000, "first_day": "2025-01-28"}
st.write("# Welcome to Portfolia!! 👋")

st.markdown(
	"""
	Invest like the insiders and take the guesswork out of building a winning portfolio—Autopilot is your gateway to smarter, data-driven investing.
	**👈 Select a demo from the sidebar** to see some examples of what Autopilot can do!
	## Want to learn more?
	Autopilot is the smart investing app that puts your money on “autopilot” by mirroring the moves of the market’s top insiders. Imagine tapping into the strategies of influential politicians, seasoned hedge fund managers, and key industry insiders—all without needing to spend hours poring over financial data.

	###Key Features:
	- Insider-Inspired Portfolios: Autopilot analyzes public portfolio data from top-performing insiders to build a diversified investment strategy tailored for you.
	- Hands-Free Investing: With automated rebalancing and real-time monitoring, your investments are managed seamlessly, letting you focus on what matters most.
	- Data-Driven Decisions: Leverage advanced analytics to replicate strategies proven by those who have a track record of success in navigating the markets.
	- User-Friendly Interface: Whether you’re new to investing or a seasoned pro, Autopilot makes it easy to get started and monitor your portfolio’s performance.
"""
)

