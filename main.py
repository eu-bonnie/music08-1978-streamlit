import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Retro & Modern Hits 78", page_icon="🎵", layout="centered")

# st.text("Olá mundo!")

# CSS parecido com o YoutubeMusic
st.markdown("""
<style>
    /* Fundo principal */
    .stApp { 
        background-color: #030303; 
        color: white; 
    }
    
    /* Container da música */
    .song-container {
        display: flex;
        align-items: center;
        background-color: #000000;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 8px;
        border-bottom: 1px solid #282828;
        transition: background-color 0.2s;
    }
    
    .song-container:hover { 
        background-color: #1a1a1a; 
    }
    
    /* Ícone de Ranking Vermelho YouTube */
    .rank-icon {
        color: #FF0000;
        font-weight: bold;
        font-size: 22px;
        margin-right: 25px;
        min-width: 40px;
        text-align: center;
    }
    
    .song-details { flex-grow: 1; }
    
    .song-title { 
        font-size: 18px; 
        font-weight: 500; 
        margin: 0; 
        color: #ffffff; 
    }
    
    .artist-name { 
        color: #aaaaaa; 
        font-size: 14px; 
        margin: 0; 
    }
    
    /* Botão Play Estilo YouTube */
    .youtube-btn {
        background-color: #FF0000;
        color: white !important;
        text-decoration: none;
        font-size: 13px;
        font-weight: bold;
        padding: 8px 16px;
        border-radius: 2px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .youtube-btn:hover { 
        background-color: #cc0000; 
    }

    /* Ajuste do Slider */
    .stSlider > div [data-baseweb="slider"] > div {
        background-image: linear-gradient(to right, #FF0000 0%, #FF0000 100%);
    }
</style>
""", unsafe_allow_html=True)

st.title("🎧 Painel Retro: Agosto 1978")
st.write("Aqui você pode explorar os maiores sucessos da Billboard Hot nos Estados Unidos durante Agosto de 78")
st.write("Arraste o slider para ver o que era mais badalado durante as semanas.")

# Carregar dados
df = pd.read_csv("data/billboard_1978.csv")
df['semana_formatada'] = pd.to_datetime(df['semana']).dt.strftime('%d/%m/%Y')

# Substitua o antigo st.slider por este seletor:
semanas_disponiveis = df['semana_formatada'].unique()
semana_escolhida = st.selectbox("Selecione a semana do ranking:", semanas_disponiveis)

# Filtragem simplificada (busca direta pela string da semana)
ranking_final = df[df['semana_formatada'] == semana_escolhida].sort_values('rank')

st.write(f"Exibindo sucessos da semana de **{semana_escolhida}**")

for _, row in ranking_final.iterrows():
    st.markdown(f"""
        <div class="song-container">
            <div class="rank-icon">{int(row['rank'])}</div>
            <div class="song-details">
                <p class="song-title">{row['titulo']}</p>
                <p class="artist-name">{row['artista']}</p>
            </div>
            <a href="{row['url_youtube']}" class="youtube-btn" target="_blank">OUVIR</a>
        </div>
    """, unsafe_allow_html=True)