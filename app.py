import streamlit as st

st.title("Conversor de Temperatura")
celsius = st.number_input("Grados Celsius")
fahrenheit = celsius * 9 / 5 + 32
st.write(f"{celsius} ºC son {fahrenheit} ºF")
