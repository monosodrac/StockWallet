# importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf

# criar as funções de carregamento de dados
    # Cotações do Itau - ITUB4 - 2010 a 2025
def carregar_dados(empresa):
    dados_acao = yf.Ticker("ITUB4")

# preparar as visualizações

# criar a interface do streamlit
st.write("""
# App preço de ações
O gráfico abaixo representa a evolução do preço das ações do Itaú (ITAUB4) ao longo dos anos
""")

st.write("""
# Fim do app
""")
