#limpeza dos dados coletados do ThingSpeak
#deixa os dados em padrões para o dataframe ser usado pela ia
import pandas as pd

def limpar(df):

    # Renomeia as colunas do ThingSpeak
    df = df.rename(columns={
        "field1": "fumaca",
        "field2": "co",
        "field3": "temperatura",
        "field4": "umidade",
        "field5": "pressao",
        "field6": "pm1",
        "field7": "pm25",
        "field8": "pm10"
    })

    # Lista das colunas dos sensores
    sensores = [
        "fumaca",
        "co",
        "temperatura",
        "umidade",
        "pressao",
        "pm1",
        "pm25",
        "pm10"
    ]

    # Converte os dados para números
    for coluna in sensores:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce")

    # Remove linhas com valores vazios
    #df = df.dropna()
    df = df.fillna(0)

    return df