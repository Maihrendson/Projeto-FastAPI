# app.py (Streamlit)
import streamlit as st
import requests

st.title("Painel Logístico - PMLI")
st.sidebar.header("Cadastrar Nova Entrega")

id = st.sidebar.number_input("ID", step=1) #
cliente = st.sidebar.text_input("Cliente")
destino = st.sidebar.text_input("Destino")
status = st.sidebar.selectbox("Status", ["Pendente", "Em Trânsito", "Entregue"])

if st.sidebar.button("Salvar Entrega"): #Cria um botão para salvar a entrega.
    data = {"id": id, "cliente": cliente, "destino": destino, "status": status}
    requests.post("http://127.0.0.1:8000/entregas/", json=data)
    st.sidebar.success("Entrega registrada!")
    
st.header("Entregas Registradas") #Exibe as entregas registradas.
response = requests.get("http://127.0.0.1:8000/entregas/")
if response.status_code == 200:
    entregas = response.json().get("entregas", [])
    for entrega in entregas:
        st.write(f"ID: {entrega[0]}, Cliente: {entrega[1]}, Destino: {entrega[2]}, Status: {entrega[3]}")
else:
    st.error("Erro ao carregar entregas.")