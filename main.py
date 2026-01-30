import streamlit as st
import pandas as pd
from datetime import datetime

# Configurações de Página
st.set_page_config(page_title="Billboard 78", page_icon="🎵", layout="centered")

# CSS para Estilo Spotify Minimalista
st.markdown("""
<style>
    body { background-color: #121212; }
    .stApp { background-color: #121212; color: white; }
    .song-container {
        display: flex;
        align-items: center;
        background-color: #181818;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
        transition: 0.3s;
    }
    .song-container:hover { background-color: #282828; }
    .rank { font-size: 24px; font-weight: bold; color: #1DB954; margin-right: 20px; width: 30px; }
    .album-art { border-radius: 4px; margin-right: 15px; }
    .song-details { flex-grow: 1; }
    .song-title { font-size: 18px; font-weight: bold; margin: 0; }
    .artist-name { color: #b3b3b3; font-size: 14px; margin: 0; }
    .spotify-btn {
        background-color: #1DB954;
        color: white !important;
        padding: 8px 16px;
        border-radius: 20px;
        text-decoration: none;
        font-size: 12px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.title("🎧 Billboard Retro: Agosto 1978")
st.write("Arraste o slider para ver o que tocava em qualquer dia do mês.")

# Carregar Dados
df = pd.read_csv("data/billboard_1978.csv")
df['inicio'] = pd.to_datetime(df['inicio'])
df['fim'] = pd.to_datetime(df['fim'])

# Filtro por Dia
dia_selecionado = st.slider("Selecione o dia de Agosto", 1, 31, 1)
data_alvo = datetime(1978, 8, dia_selecionado)

# Lógica de Filtro (Verifica se a data está no intervalo)
ranking_dia = df[(df['inicio'] <= data_alvo) & (df['fim'] >= data_alvo)].sort_values('rank')

st.markdown("---")

# Exibição
if not ranking_dia.empty:
    for _, row in ranking_dia.iterrows():
        st.markdown(f"""
            <div class="song-container">
                <div class="rank">{int(row['rank'])}</div>
                <img src="{row['url_imagem']}" class="album-art" width="60" height="60">
                <div class="song-details">
                    <p class="song-title">{row['titulo']}</p>
                    <p class="artist-name">{row['artista']}</p>
                </div>
                <a href="{row['url_spotify']}" class="spotify-btn" target="_blank">OUVIR</a>
            </div>
        """, unsafe_allow_html=True)
else:
    st.error("Dados não encontrados para este dia.")

st.caption("Dados históricos baseados na Billboard Hot 100.")