import streamlit as st
import plot


st.header('3D - Volatility Surface')
st.sidebar.subheader("Settings")
ticker = st.sidebar.text_input("Ticker", value='AAPL', max_chars=10, autocomplete='offer')
risk_free_interest_rate = st.sidebar.number_input("Risk Free Interest Rate (%)", value=5.0)


# graph

st.pyplot(plot.graph_volatility())
calculate = st.sidebar.button("Calculate")