from src.coleta.thingspeak import obter_dados
from src.processamento.limpeza import limpar

df = obter_dados()


df = limpar(df)

print(df.head())