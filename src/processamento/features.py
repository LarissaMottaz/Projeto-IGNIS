# transformação de leituras brutas dos sensores em features para o modelo de IA (cria informações mais relevantes a partir dos dados coletados)
# features e normalização são fundamentais em qualquer projeto de Machine Learning. 
# Eles fazem parte do pré-processamento, que prepara os dados para que a rede neural consiga aprender corretamente.

import numpy as np
from configs.sensores import SENSORES
from configs.ia import JANELA_CURTA
def criar_features_ambientais(df):

#B1 Features ambientais
 # 1) Índice de Secura smbiental
   df["indice_secura"] = (
    df["temperatura_norm"]
    *
    (1 - df["umidade_norm"])
    )

    # 2) Índice de Poluição atmosférica
   df["indice_poluicao"] = (
    0.20 * df["co_norm"]
    +
    0.25 * df["fumaca_norm"]
    +
    0.20 * df["pm1_norm"]
    +
    0.20 * df["pm25_norm"]
    +
    0.15 * df["pm10_norm"]
)
    # 3) Índice de Combustão
   df["indice_combustao"] = (
    0.40 * df["fumaca_norm"]
    +
    0.35 * df["co_norm"]
    +
    0.25 * df["pm25_norm"]
)
    # 4) indice de Material Particulado
   df["indice_particulas"] = (
    df["pm1_norm"]
    +
    df["pm25_norm"]
    +
    df["pm10_norm"]
) / 3
   # 5) indice termico
   df["indice_termico"] = (
    0.50 * df["temperatura_norm"]
    +
    0.30 * (1 - df["umidade_norm"])
    +
    0.20 * (1 - df["pressao_norm"])
)
   # 6) indice atmosferico
   df["indice_atmosferico"] = (
    0.50 * df["pressao_norm"]
    +
    0.50 * df["umidade_norm"]
)
   # 7) indice inicial de risco de queimadas
   df["indice_risco"] = (
    0.30 * df["indice_secura"]
    +
    0.40 * df["indice_combustao"]
    +
    0.30 * df["indice_poluicao"]
)
   # 8) indice de estabilidade ambiental
   df["indice_estabilidade"] = (1 -df["indice_risco"]
)
   return df

#B2 Features relacionais

def criar_features_relacionais(df):

    df["relacao_co_fumaca"] = (df["co_norm"] /(df["fumaca_norm"] + 0.001)
    )

    df["relacao_pm25_pm10"] = ( df["pm25_norm"] /(df["pm10_norm"] + 0.001)
    )

    df["relacao_pm1_pm25"] = (df["pm1_norm"] /(df["pm25_norm"] + 0.001)
    )

    df["temp_umidade"] = (df["temperatura_norm"] *(1 - df["umidade_norm"])
    )

    df["temp_co"] = (df["temperatura_norm"] *df["co_norm"]
    )

    df["temp_pm25"] = (df["temperatura_norm"] *df["pm25_norm"]
    )

    df["umidade_fumaca"] = ( (1 - df["umidade_norm"]) *df["fumaca_norm"]
    )

    df["co_pm25"] = (df["co_norm"] *df["pm25_norm"]
    )

    df["pressao_umidade"] = (df["pressao_norm"] * df["umidade_norm"]
    )

    df["pressao_temperatura"] = (df["pressao_norm"] *df["temperatura_norm"]
    )

    return df

#B3 Dinâmica temporal
def criar_features_dinamicas(df):
   
   for sensor, dados in SENSORES.items():

    if not dados["usar_delta"]:
        continue

    coluna = f"{sensor}_norm"

    df[f"delta_{sensor}"] = df[coluna].diff()

    df[f"intensidade_{sensor}"] = (
        df[f"delta_{sensor}"].abs()
    )

    df[f"direcao_{sensor}"] = np.sign(
        df[f"delta_{sensor}"]
    )

    df[f"aceleracao_{sensor}"] = (
        df[f"delta_{sensor}"].diff()
    )

        # Δ (variação entre leituras)
    df[f"delta_{sensor}"] = df[coluna].diff()

        # Intensidade da mudança
    df[f"intensidade_{sensor}"] = (
            df[f"delta_{sensor}"].abs()
        )

        # Direção da mudança
    df[f"direcao_{sensor}"] = np.sign(
            df[f"delta_{sensor}"]
        )

    # Remove NaN gerado pelo diff()
    df.fillna(0, inplace=True)

    return df

#B4 Tendencia 
def criar_features_tendencia(df):
    janela = JANELA_CURTA

    for sensor, dados in SENSORES.items():

        if not dados["usar_tendencia"]:
            continue

        coluna = f"{sensor}_norm"

        df[f"media_{sensor}"] = ( df[coluna].rolling(

                window=janela,min_periods=1) .mean()
        )

        df[f"desvio_{sensor}"] = (

            df[coluna]

            .rolling(window=janela,min_periods=1) .std()
        )
        df[f"tendencia_{sensor}"] = (

            df[coluna] - df[f"media_{sensor}"]
        )
        df[f"direcao_tendencia_{sensor}"] = np.sign(df[f"tendencia_{sensor}"]
        )

    df.fillna(0, inplace=True)

    return df

#B5 Velocidade de mudança

def criar_features_velocidade(df):

    janela = 5

    for sensor in SENSORES.keys():

        df[f"velocidade_{sensor}"] = (

            df[f"delta_{sensor}"] .rolling(

                window=janela,min_periods=1 ) .mean()
        )

        df[f"intensidade_velocidade_{sensor}"] = ( df[f"velocidade_{sensor}"].abs()

        )

        df[f"direcao_velocidade_{sensor}"] = np.sign(df[f"velocidade_{sensor}"])

        df[f"velocidade_relativa_{sensor}"] = (

            df[f"velocidade_{sensor}"] / ( df[f"intensidade_{sensor}"] + 0.001 )  )

    df.fillna(0, inplace=True)

    return df

#B6 Memória

def calcular_persistencia(serie, limite, tipo_risco):
  
    contador = []
    tempo = 0

    for valor in serie:

        if tipo_risco == "maior_valor_maior_risco":

            if valor >= limite:
                tempo += 1
            else:
                tempo = 0

        elif tipo_risco == "menor_valor_maior_risco":

            if valor <= limite:
                tempo += 1
            else:
                tempo = 0

        else:
            tempo = 0

        contador.append(tempo)

    return contador

def criar_features_memoria(df):

    for sensor, dados in SENSORES.items():

        coluna = f"{sensor}_norm"

        # Memória curta
        df[f"memoria_curta_{sensor}"] = (
            df[coluna]
            .rolling(window=dados["janela_memoria"]["curta"],min_periods=1)
            .mean()
        )

        # Memória média
        df[f"memoria_media_{sensor}"] = (
            df[coluna]
            .rolling(window=dados["janela_memoria"]["media"],min_periods=1)
            .mean()
        )

        # Memória longa
        df[f"memoria_longa_{sensor}"] = (
            df[coluna]
            .rolling(window=dados["janela_memoria"]["longa"],min_periods=1)
            .mean()
        )

        # Persistência
        df[f"persistencia_{sensor}"] = calcular_persistencia(
            serie=df[coluna],
            limite=dados["limiar_memoria"],
            tipo_risco=dados["direcao_risco"]
        )

    df.fillna(0, inplace=True)

    return df

# estado ambiental integrado (EAI)
#Feature desenvolvida para representar o estado global
#do ambiente considerando simultaneamente todos os sensores 
#O cálculo utiliza as memórias de curto prazo dos
#sensores ponderadas pela importância ambiental de cada variável.
#Resultado:
#0  -> ambiente totalmente estável
#1  -> ambiente extremamente crítico

def criar_estado_sensores(df):
     for sensor, dados in SENSORES.items():

        if not dados["usar_eai"]:
            continue
        curta = df[f"memoria_curta_{sensor}"]
        media = df[f"memoria_media_{sensor}"]
        longa = df[f"memoria_longa_{sensor}"]
        estado = (
            0.50 * curta +
            0.30 * media +
            0.20 * longa
        )
        # sensores cujo risco aumenta quando o valor DIMINUI
        if dados["direcao_risco"] == "menor_valor_maior_risco":
            estado = 1 - estado
        df[f"estado_{sensor}"] = estado

        return df

# Estado Ambiental Integrado

def criar_eai(df):

    soma = 0
    soma_pesos = 0

    for sensor, dados in SENSORES.items():

        if not dados["usar_eai"]:
         continue

    peso = dados["peso"]

    soma += peso * df[f"estado_{sensor}"]

    soma_pesos += peso

    df["EAI"] = soma / soma_pesos

    return df

# Persistência do estado ambiental

def criar_persistencia_eai(df):
    contador = []
    tempo = 0
    for valor in df["EAI"]:
        if valor >= 0.70:
            tempo += 1
        else:
            tempo = 0
        contador.append(tempo)  
        df["EAI_persistencia"] = contador

    return df

# Tendência do estado ambiental

def criar_tendencia_eai(df):

    df["EAI_tendencia"] = (

    df["EAI"] - df["EAI"] .rolling(  window=5,  min_periods=1  )  .mean() )

    return df

# Velocidade do estado ambiental

def criar_velocidade_eai(df):

    df["EAI_velocidade"] = ( df["EAI"]  .diff()  )

    df["EAI_velocidade"] = (df["EAI_velocidade"].fillna(0)  )

    return df

# Direção da mudança ambiental

def criar_direcao_eai(df):

    df["EAI_direcao"] = np.sign(df["EAI_velocidade"])

    return df

# Intensidade da mudança

def criar_intensidade_eai(df):

    df["EAI_intensidade"] = ( df["EAI_velocidade"]  .abs() )

    return df

# Aceleração do estado ambiental

def criar_aceleracao_eai(df):

    df["EAI_aceleracao"] = ( df["EAI_velocidade"].diff())
    df["EAI_aceleracao"] = ( df["EAI_aceleracao"] .fillna(0))

    return df
# Índice de severidade ambiental

def criar_severidade_eai(df):
    df["EAI_severidade"] = (df["EAI"] *(1 + df["EAI_persistencia"] / 10) )
    df["EAI_severidade"] = (df["EAI_severidade"].clip(0, 1))
    return df
# Função principal
def criar_features_eai(df):
    df = criar_estado_sensores(df)
    df = criar_eai(df)
    df = criar_persistencia_eai(df)
    df = criar_tendencia_eai(df)
    df = criar_velocidade_eai(df)
    df = criar_direcao_eai(df)
    df = criar_intensidade_eai(df)
    df = criar_aceleracao_eai(df)
    df = criar_severidade_eai(df)

    return df

#B7 Contexto

def criar_features_contexto(df):

    # 1. Estado Climático
    df["estado_climatico"] = (
        0.45 * df["temperatura_norm"] + 0.35 * (1 - df["umidade_norm"])+  0.20 * (1 - df["pressao_norm"])

    )
    # 2. Estado da Combustão
    df["estado_combustao"] = (

        0.50 * df["fumaca_norm"] + 0.35 * df["co_norm"] + 0.15 * df["pm25_norm"]
    )
    # 3. Estado da Poluição
    df["estado_poluicao"] = (

        0.20 * df["pm1_norm"]+  0.40 * df["pm25_norm"] + 0.20 * df["pm10_norm"]  + 0.20 * df["co_norm"]

    )
    # 4. Estado de Secura
    df["estado_secura"] = (
        0.70 * df["indice_secura"] +0.30 * df["indice_termico"]
    )
    # 5. Contexto Atmosférico
    df["contexto_atmosferico"] = (
        0.60 * df["indice_atmosferico"]+0.40 * df["estado_climatico"]
    )
    # 6. Contexto Ambiental Global
    df["contexto_global"] = (
        0.25 * df["estado_climatico"] +
        0.25 * df["estado_combustao"] +0.20 * df["estado_poluicao"]  +
        0.15 * df["estado_secura"]  + 0.15 * df["contexto_atmosferico"]

    )
    # 7. Memória do Contexto
    df["memoria_contexto"] = (
        df["contexto_global"].rolling(window=10, min_periods=1).mean()
    )
    # 8. Persistência do Contexto
    persistencia = []
    tempo = 0
    for valor in df["contexto_global"]:
        if valor >= 0.70:
            tempo += 1
        else:
            tempo = 0
        persistencia.append(tempo)
    df["persistencia_contexto"] = persistencia
    # 9. Tendência do Contexto
    df["tendencia_contexto"] = (
        df["contexto_global"]  - df["contexto_global"] .rolling(window=5, min_periods=1) .mean()
    )
    # 10. Velocidade do Contexto
    df["velocidade_contexto"] = (
        df["contexto_global"] .diff()
    )
    # 11. Direção do Contexto
    df["direcao_contexto"] = np.sign(
        df["velocidade_contexto"]
    )
    # 12. Intensidade da Mudança
    df["intensidade_contexto"] = (
        df["velocidade_contexto"] .abs()
    )

    # 13. Aceleração do Contexto
    df["aceleracao_contexto"] = (
        df["velocidade_contexto"]
        .diff()
    )
    # 14. Severidade Ambiental

    df["severidade_contexto"] = (
        df["contexto_global"]  * ( 1 + df["persistencia_contexto"] / 10
        )
    )
    df["severidade_contexto"] = (
        df["severidade_contexto"]
        .clip(0,1)
    )
    # 15. Estado Ambiental Discreto
    df["classe_contexto"] = np.select(

        [
            df["contexto_global"] < 0.30,
            df["contexto_global"] < 0.50,
            df["contexto_global"] < 0.70,
            df["contexto_global"] >= 0.70
        ],
        [
            "Estável",
            "Atenção",
            "Alerta",
            "Crítico"
        ]
    )
    df.fillna(0, inplace=True)

    return df

#B8 janela temporal


#Depois criaremos um módulo chamado sequencias.py, que transformará as leituras do ThingSpeak em janelas temporais (por exemplo, os últimos 10 registros). Esse tipo de representação é muito mais adequado para 
# previsão de queimadas e prepara o projeto para evoluir de uma MLP para uma LSTM ou GRU no futuro, sem precisar reconstruir toda a arquitetura.

def executar_features(df):

    df = criar_features_ambientais(df)

    df = criar_features_relacionais(df)

    df = criar_features_dinamicas(df)

    df = criar_features_tendencia(df)

    df = criar_features_velocidade(df)

    df = criar_features_memoria(df)

    df = criar_features_contexto(df)

    df = criar_features_eai

    return df