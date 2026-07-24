#Módulo de Normalização
#Responsável por:
# Validar dados
# Corrigir valores inválidos
# Aplicar limites ambientais
# Normalizar usando Min-Max
# Criar colunas normalizadas
# Gerar estatísticas

#transforma unidade dos dados para a ia aprender

import os
import pickle
import numpy as np
import logging
import pandas as pd
from configs.sensores import SENSORES

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def validar_dataframe(df):

    if df is None:
        raise ValueError("DataFrame inexistente.")

    if df.empty:
        raise ValueError("DataFrame vazio.")

    return True

def validar_colunas(df):

    faltando=[]

    for sensor in SENSORES:

        if sensor not in df.columns:

            faltando.append(sensor)

    if faltando:

        raise ValueError(

            f"Colunas ausentes: {faltando}"

        )
    return True

def converter_para_numerico(df):

    df = df.copy()

    for sensor in SENSORES:

        df[sensor] = pd.to_numeric(
            df[sensor],
            errors="coerce"
        ).astype(float)

    return df

def tratar_valores_ausentes(df):

    df = df.copy()

    for sensor in SENSORES:
        if sensor in df.columns:
            df[sensor] = df[sensor].interpolate(method="linear")

    df = df.ffill()

    df = df.bfill()

    return df


def validar_valores(df):

    relatorio = {}

    for sensor,dados in SENSORES.items():

        minimo=dados["min"]

        maximo=dados["max"]

        mascara=(

            (df[sensor]<minimo)

            |

            (df[sensor]>maximo)

        )
        quantidade = mascara.sum()

        relatorio[sensor] = quantidade

        if quantidade > 0:

            logging.warning(
                f"{sensor}: {quantidade} valores fora da faixa."
            )

    return df, relatorio

def limitar_valores(df):

    for sensor,dados in SENSORES.items():

        df[sensor]=df[sensor].clip(

            lower=dados["min"],

            upper=dados["max"]

        )
    return df
def normalizar_sensor(serie, minimo, maximo):

    if maximo == minimo:

        raise ValueError(

            f"Erro na configuração do sensor. "

            f"min == max ({minimo})"

        )

    return (

        serie - minimo ) / ( maximo - minimo

    )
def normalizar_dataframe(df):

    df=df.copy()

    for sensor,dados in SENSORES.items():

        df[f"{sensor}_norm"]=normalizar_sensor(

            df[sensor].astype(float),

            dados["min"],

            dados["max"]

        ).astype(float)

    return df

def obter_estatisticas(df):

    estatisticas={}

    for sensor in SENSORES:

        estatisticas[sensor]={

            "min":float(df[sensor].min()),

            "max":float(df[sensor].max()),

            "media":float(df[sensor].mean()),

            "desvio":float(df[sensor].std())

        }

    return estatisticas

def salvar_normalizador():
    os.makedirs("models", exist_ok=True)

    with open(

        "models/normalizador.pkl",

        "wb"

    ) as arquivo:

        pickle.dump(SENSORES,arquivo)

def carregar_normalizador():

    with open("models/normalizador.pkl", "rb") as arquivo:

        return pickle.load(arquivo)

def executar_normalizacao(df):

    validar_dataframe(df)

    validar_colunas(df)

    df = converter_para_numerico(df)

    df = tratar_valores_ausentes(df)

    df, relatorio = validar_valores(df)

    df = limitar_valores(df)

    df = normalizar_dataframe(df)

    estatisticas = obter_estatisticas(df)

    salvar_normalizador()

    logging.info("Normalização concluída com sucesso.")

    return df