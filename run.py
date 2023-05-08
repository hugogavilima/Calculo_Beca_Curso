import streamlit as st

st.set_page_config(layout="wide", page_title="Cálculo Porcentaje de Beca")


st.write("# Cálculo Porcentaje de Beca")
st.write(
    "La aplicación permite consultar el porcentaje de beca de cada estudiante."
    )


a, b, c  = st.columns(3)

with b:
    st.text_input("Favor ingrese la cédula del estudiante.")

