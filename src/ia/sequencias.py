#tranforma as features em sequencias 
#Transforma o DataFrame contínuo de 
#features em tensores/matrizes 3D para redes de séries temporais:
import numpy as np
import pandas as pd
from configs.ia import (
    TAMANHO_JANELA,
    HORIZONTE_PREVISAO,
    ALVO,
    TESTE,
    TIPO_MODELO,
    SENSORES_PREVISAO,
    LIMIAR_RISCO
)
from sklearn.model_selection import train_test_split
from configs.pesos_features import FEATURES

def selecionar_features(df):

    colunas = []

    for feature, dados in FEATURES.items():

        if dados["usar"]:

            if feature in df.columns:

                colunas.append(feature)
                colunas = sorted(colunas)

    return df[colunas]

def criar_dataset(df):

    dados = selecionar_features(df)

    limite = len(df) - TAMANHO_JANELA - HORIZONTE_PREVISAO + 1

    X = []
    y = []

    for i in range(limite):
        janela = dados.iloc[i : i + TAMANHO_JANELA].values
        X.append(janela)

        indice_alvo = i + TAMANHO_JANELA + HORIZONTE_PREVISAO - 1

        if TIPO_MODELO == "regressao":
            y.append(df.iloc[indice_alvo][ALVO])
        elif TIPO_MODELO == "classificacao":
            valor = df.iloc[indice_alvo][ALVO]
            y.append(1 if valor >= LIMIAR_RISCO else 0)
        elif TIPO_MODELO == "multivariado":
            y.append(df.iloc[indice_alvo][SENSORES_PREVISAO].values)
        else:
            raise ValueError(f"Tipo de modelo inválido: {TIPO_MODELO}")

    X = np.array(X, dtype=np.float32)
    y = np.array(y, dtype=np.float32)

    return X, y

def dividir_dataset(
    X,
    y,
    teste=TESTE,
    random_state=42
):
    return train_test_split( X, y,test_size=teste, random_state=random_state,
        shuffle=False

    )
def preparar_dataset(df):

    X, y = criar_dataset(df)

    validar_dataset(X, y)

    return dividir_dataset( X, y,)

def validar_dataset(X, y):

    print(f"Amostras: {len(X)}")

    print(f"X: {X.shape}")

    print(f"y: {y.shape}")

    if len(X) != len(y):

        raise ValueError(
            "X e y possuem tamanhos diferentes."
        )

    print("Dataset válido.")

def mostrar_dataset(X, y):

    print()

    print("Formato das entradas")

    print(X.shape)

    print()

    print("Formato das saídas")

    print(y.shape)

    print()

    print("Primeira sequência")

    print(X[0])

    print()

    print("Primeiro alvo")

    print(y[0])