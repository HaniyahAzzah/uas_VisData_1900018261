
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np
import matplotlib.pyplot as plt

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
# Streamlit page configuration 
st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

st.title(":traffic_light: Data Penindakan Pelanggaran Lalu Lintas dan Angkutan Jalan Tahun 2021 Bulan Januari-Juli")
st.markdown("#")

# ---- READ EXCEL ----
df = pd.read_excel(
    io="Dataset_HaniyahAzzahUlfah-1900018261- UAS_VisDat_genap2021.xlsx",
    engine="openpyxl",
    sheet_name="Sheet1",
    usecols="A:J",
    nrows=43,
)

# ---- SIDEBAR ----
st.sidebar.header("Anda Bisa Memfilter Data Disini :")
wilayah = st.sidebar.multiselect(
    "Pilih Berdasarkan Wilayah:",
    options=df["wilayah"].unique(),
    default=df["wilayah"].unique()
)

Bulan = st.sidebar.multiselect(
    "Pilih Berdasarkan Bulan:",
    options=df["Bulan"].unique(),
    default=df["Bulan"].unique()
)

df_selection = df.query(
    "wilayah == @wilayah & Bulan ==@Bulan"
)

st.dataframe(df_selection) # view dataframe on page

#---MAINPAGE---

st.markdown("##")

total_bap = int(df_selection["bap_tilang"].sum())
total_bap_polisi = int(df["bap_polisi"].sum())
rata_bap_tilang = int(df_selection["bap_tilang"].mean())
rata_bap_polisi = int(df_selection["bap_polisi"].mean())

left_column, middle_column, right_column = st.columns(3)
with left_column:
        st.subheader("Total BAP Tilang")
        st.subheader(f"{total_bap:,}")
with middle_column:
        st.subheader("Total BAP Polisi:cop:")
        st.subheader(f"{total_bap_polisi:,}")
with right_column:
    st.subheader("Rata-Rata BAP Tilang :bar_chart:")
    st.subheader(f"{rata_bap_tilang:,}")
with left_column:
    st.subheader("Rata-Rata BAP Polisi :bar_chart:")
    st.subheader(f"{rata_bap_polisi:,}")

        
st.markdown("""---""")
st.text("Grafik garis BAP Tilang, BAP Polisi, dan tindakan angkut motor  ")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['bap_tilang', 'bap_polisi','angkut_motor'])
    

st.line_chart(chart_data)


#========================================================

baptilang_by_wilayah_line = (
    df_selection.groupby(by=["wilayah"]).sum()[["bap_tilang"]].sort_values(by="wilayah")
    
)
fig_baptilang = px.bar(
    baptilang_by_wilayah_line,
    orientation="h",
    title="<b>BAP Tilang Berdasarkan Wilayah</b>",
    color_discrete_sequence=["#0083B8"] * len(baptilang_by_wilayah_line),
    template="plotly_white",
)
fig_baptilang.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_baptilang, use_container_width=True)

#===========================================================

