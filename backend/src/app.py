import streamlit as st
import requests
import pandas as pd

# Função para obter dados da API
def get_producao_data(ano):
    url = f"http://localhost:5000/api/producao?ano={ano}"
    try:
        response = requests.get(url)
        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Erro ao acessar a API: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Erro ao fazer a requisição: {e}")
        return None

# Função para mostrar os dados
def show_data(data):
    if data:
        # Exibindo informações gerais
        st.write(f"**Ano: {data['ano']}**")
        st.write(f"**Total de Produção: {data['total']}**")

        # Convertendo os dados para um formato tabular
        for item in data['dados']:
            produto = item['produto']
            quantidade = item['quantidade']
            subprodutos = item['subprodutos']
            
            # Exibindo os dados principais do produto
            st.subheader(f"Produto: {produto} - Quantidade: {quantidade}")
            
            # Exibindo os subprodutos
            if subprodutos:
                df_subprodutos = pd.DataFrame(subprodutos)
                st.write(df_subprodutos)

# Título do aplicativo Streamlit
st.title("Consulta de Produção por Ano")

# Campo para seleção do ano
ano_selecionado = st.slider("Escolha o ano", min_value=2010, max_value=2023, value=2017, step=1)

# Quando o ano for selecionado, fazemos a consulta
st.write(f"Consultando os dados para o ano {ano_selecionado}...")

# Obter os dados da API
dados = get_producao_data(ano_selecionado)

# Exibir os dados obtidos
show_data(dados)
