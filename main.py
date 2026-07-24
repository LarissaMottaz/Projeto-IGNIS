from src.coleta.thingspeak import obter_dados
from src.processamento.features import executar_features
from src.processamento.limpeza import limpar

df = obter_dados()

df = executar_features(df)

df = limpar(df)

df = carregar_dados(df)

df = executar_normalizacao(df)

df = calcular_ica(df)

print(df.head())