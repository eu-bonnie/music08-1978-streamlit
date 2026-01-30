# src/database.py
import pandas as pd

def carregar_dados(caminho_csv):
    """Lê o CSV e prepara as colunas de data."""
    df = pd.read_csv(caminho_csv)
    # Converte para datetime e cria a versão formatada para o usuário
    df['semana_formatada'] = pd.to_datetime(df['semana']).dt.strftime('%d/%m/%Y')
    return df

def filtrar_por_semana(df, semana_escolhida):
    """Filtra o DataFrame pela semana selecionada e ordena pelo rank."""
    return df[df['semana_formatada'] == semana_escolhida].sort_values('rank')