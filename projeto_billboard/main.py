import streamlit as st
from src.database import carregar_dados, filtrar_por_semana

# Configuração da página
st.set_page_config(page_title="Retro & Modern Hits 78", page_icon="🎵", layout="centered")

# Injeção do CSS externo
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Cabeçalho
st.title("🎧 Painel Retro: Agosto 1978")
st.write("Explore os maiores sucessos da Billboard Hot 100 durante Agosto de 78.")

try:
    # Carregamento de dados usando a lógica da pasta src
    df = carregar_dados("data/music.csv")
    
    # Interface de seleção
    semanas_disponiveis = df['semana_formatada'].unique()
    semana_escolhida = st.selectbox("Selecione a semana do ranking:", semanas_disponiveis)
    
    # Filtragem
    ranking_final = filtrar_por_semana(df, semana_escolhida)

    st.write(f"Exibindo sucessos da semana de **{semana_escolhida}**")

    # Renderização dos itens
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

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")