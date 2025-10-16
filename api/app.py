# app.py (Streamlit)
import streamlit as st
import requests

st.title("Painel Logístico - PMLI")
st.sidebar.header("Cadastrar Nova Entrega")

id = st.sidebar.number_input("ID", step=1)
cliente = st.sidebar.text_input("Cliente")
destino = st.sidebar.text_input("Destino")
status = st.sidebar.selectbox("Status", ["Pendente", "Em Trânsito", "Entregue"])

if st.sidebar.button("Salvar Entrega"):
    data = {"id": id, "cliente": cliente, "destino": destino, "status": status}
    requests.post("http://127.0.0.1:8000/entregas/", json=data)
    st.sidebar.success("Entrega registrada!")