"""

Top 5 Cryptocurency Daily Prices Webapp

- Using streamlit and Yahoo Finance


"""

import yfinance as yf #Yahoo finance to get stock data
import streamlit as st #Streamlit to create the webapp
from PIL import Image #Import Pillow to add icons
from urllib.request import urlopen #To add URLS


st.write("""

# Top 5 Cryptocurrency Daily Prices


## Bitcoin $USD 
""")

#Define bitcoin and ethereum abbreviation used by Yahoo Finance.
BTC_abbv = 'BTC-USD'
ETH_abbv = 'ETH-USD'
XRP_abbv = 'XRP-USD'
BCH_abbv = 'BCH-USD'
LTC_abbv = 'LTC'

#Lets access the Data from Yahoo Finance using .ticker method
BTC_Data = yf.Ticker(BTC_abbv)
ETH_Data = yf.Ticker(ETH_abbv)
XRP_Data = yf.Ticker(XRP_abbv)
BCH_Data = yf.Ticker(BCH_abbv)
LTC_Data = yf.Ticker(LTC_abbv)


#Lets fetch the Price History from Yahoo Finance. We use Max Period to get all the History
BTCHis = BTC_Data.history(period="max") 
EthHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")
LTCHis = LTC_Data.history(period="max")

#Adding icon for BTC
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC, use_column_width=False)

#Create a line chart from BTC-USD Close Price history
st.line_chart(BTCHis.Close)

st.write(""" ## Ethereum $USD """)

#Adding icon for ETH
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageETH, use_column_width=False)

#Create a line chart from ETH-USD Close Price history
st.line_chart(EthHis.Close)

st.write(""" ## Ripple(XRP) $USD """)

#Adding icon for XRP
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageXRP, use_column_width=False)

#Create a line chart from XRP-USD Close Price history
st.line_chart(XRPHis.Close)

st.write(""" ## Bitcoin Cash $USD """)

#Adding icon for BCH
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
st.image(imageBCH, use_column_width=False)

#Create a line chart from BCH-USD Close Price history
st.line_chart(BCHHis.Close)

st.write(""" ## Litecoin $USD """)

#Adding icon for LTC
imageLTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/2.png'))
st.image(imageLTC, use_column_width=False)

#Create a line chart from LTC-USD Close Price history
st.line_chart(LTCHis.Close)