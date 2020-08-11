"""

Cryptocurency Daily Prices Webapp

- Using streamlit and Yahoo Finance


"""

import yfinance as yf  # Yahoo finance to get stock data
import streamlit as st  # Streamlit to create the webapp
from PIL import Image  # Import Pillow to add icons
from urllib.request import urlopen  # To add URLS

st.write("""

# Cryptocurrency Daily Prices


## Bitcoin $USD
""")

# Define bitcoin and ethereum and other cryptocurrency abbreviation used by Yahoo Finance.
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
Bitcoin_Cash = 'BCH-USD'
Litecoin = 'LTC-USD'
Chainlink = 'LINK-USD'
Cardano = 'ADA-CAD'

# Lets access the Data from Yahoo Finance using .ticker method
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(Bitcoin_Cash)
LTC_Data = yf.Ticker(Litecoin)
LINK_Data = yf.Ticker(Chainlink)
ADA_Data = yf.Ticker(Cardano)

# Lets fetch the Price History from Yahoo Finance. We use Max Period to get all the History
BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")
LTCHis = LTC_Data.history(period="max")
LINKHis = LINK_Data.history(period="max")
ADAHis = ADA_Data.history(period="max")

# Adding icon for BTC
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC, use_column_width=False)

# Create a line chart from BTC-USD Close Price history
st.line_chart(BTCHis.Close,  use_container_width=True)

st.write(""" ## Ethereum $USD """)

# Adding icon for ETH
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageETH, use_column_width=False)

# Create a line chart from ETH-USD Close Price history
st.line_chart(ETHHis.Close,  use_container_width=True)

st.write(""" ## Ripple $USD """)

# Adding icon for XRP
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageXRP, use_column_width=False)

# Create a line chart from XRP-USD Close Price history
st.line_chart(XRPHis.Close,  use_container_width=True)

st.write(""" ## Bitcoin-Cash $USD """)

# Adding icon for BCH
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
st.image(imageBCH, use_column_width=False)

# Create a line chart from BCH-USD Close Price history
st.line_chart(BCHHis.Close,  use_container_width=True)

st.write(""" ## Chainlink $USD """)

# Adding icon for Chainlink
imageLINK = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1975.png'))
st.image(imageLINK, use_column_width=False)

# Create a line chart from LINK-USD Close Price history
st.line_chart(LINKHis.Close,  use_container_width=True)

st.write(""" ## Litecoin $USD """)

# Adding icon for LTC
imageLTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/2.png'))
st.image(imageLTC, use_column_width=False)

# Create a line chart from LTC-USD Close Price history
st.line_chart(LTCHis.Close,  use_container_width=True)

st.write(""" ## Cardano $USD """)

# Adding icon for Cardano
imageADA = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png'))
st.image(imageADA, use_column_width=False)

# Create a line chart from ADA-USD Close Price history
st.line_chart(ADAHis.Close,  use_container_width=True)
