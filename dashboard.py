import streamlit as st, numpy as np, pandas as pd, plotly.express as px
st.set_page_config(page_title="Pipeline Analytics Dashboard", page_icon="💎")
st.title("Pipeline Analytics Dashboard")
st.markdown("Feito com ciência, carinho e o *caos domado*! 😉")

if st.button("Domar o Caos!"):
    st.balloons()
    st.success("Caos DOMADO com sucesso!")

np.random.seed(42)
data = pd.DataFrame({
    "Dia": range(1, 31),
    "Performance": np.random.normal(100, 20, 30),
    "Caos_Level": np.random.uniform(0, 10, 30),
})
fig = px.line(data, x="Dia", y=["Performance","Caos_Level"],
              title="Performance vs. Nível de Caos",
              labels={"value":"Valor","variable":"Métrica"})
fig.update_layout(showlegend=True, plot_bgcolor="white", title_x=0.5)
st.plotly_chart(fig, use_container_width=True)
