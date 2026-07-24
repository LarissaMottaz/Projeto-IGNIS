from src.coleta.thingspeak import obter_dados
from src.processamento.features import executar_features
from src.processamento.limpeza import limpar
from src.processamento.normalizacao import executar_normalizacao
from src.processamento.qualidade import calcular_ica


df = obter_dados()

df = limpar(df)

df = executar_normalizacao(df)

df = executar_features(df)

df = calcular_ica(df)

print(df.head())