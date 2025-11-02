# importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf

# criar as funções de carregamento de dados
    # Cotações do Itau - ITUB4 - 2010 a 2025
@st.cache_data
def load_data(stock):
    stock_data = yf.Ticker(stock)
    share_quotes = stock_data.history(start="2010-01-01", end="2025-10-01")
    share_quotes = share_quotes[["Close"]]
    return share_quotes

# preparar as visualizações
data = load_data("ITUB4.SA")
print(data)

# criar a interface do streamlit
st.write("""
# App preço de ações
O gráfico abaixo representa a evolução do preço das ações do Itaú (ITAUB4) ao longo dos anos
""")

# criar o gráfico
st.line_chart(data)

st.write("""
# Fim do app
""")
