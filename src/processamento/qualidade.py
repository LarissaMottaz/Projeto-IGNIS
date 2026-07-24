#Módulo de Qualidade dos Dados
#verifica dados absurdos
#Responsável por calcular o Índice de Confiabilidade Ambiental (ICA)
import pandas as pd

from configs.ica import (
    PESOS_ICA,
    PENALIDADES,
    LIMITES_VARIACAO,
    REGRAS_CONSISTENCIA
)

# INTEGRIDADE

def calcular_integridade(linha):
    """
    Calcula a porcentagem de valores válidos na leitura.
    """

    total = len(linha)
    validos = linha.notna().sum()

    return validos / total

# COBERTURA

def calcular_cobertura(linha):
    """
    Calcula a quantidade de sensores que responderam.
    """

    total = len(linha)
    ativos = linha.notna().sum()

    return ativos / total

# CONSISTÊNCIA FÍSICA

def calcular_consistencia(linha):

    score = 1.0

    # CO alto sem fumaça

    regra = REGRAS_CONSISTENCIA["co_alto_sem_fumaca"]

    if (
        linha["co"] > regra["condicao"]["co_min"]
        and
        linha["fumaca"] < regra["condicao"]["fumaca_max"]
    ):
        score -= regra["penalidade"]

    # PM2.5 alto sem fumaça

    regra = REGRAS_CONSISTENCIA["pm25_alto_sem_fumaca"]

    if (
        linha["pm25"] > regra["condicao"]["pm25_min"]
        and
        linha["fumaca"] < regra["condicao"]["fumaca_max"]
    ):
        score -= regra["penalidade"]

    # Temperatura alta + Umidade alta

    regra = REGRAS_CONSISTENCIA["temperatura_alta_umidade_alta"]

    if (
        linha["temperatura"] > regra["condicao"]["temperatura_min"]
        and
        linha["umidade"] > regra["condicao"]["umidade_min"]
    ):
        score -= regra["penalidade"]

    # PM10 não pode ser menor que PM2.5

    regra = REGRAS_CONSISTENCIA["pm10_menor_pm25"]

    if linha["pm10"] < linha["pm25"]:
        score -= regra["penalidade"]

    return max(score, 0)

# ESTABILIDADE TEMPORAL

def calcular_estabilidade(df, indice):

    if indice == 0:
        return 1.0

    score = 1.0

    anterior = df.iloc[indice - 1]
    atual = df.iloc[indice]

    if abs(atual["temperatura"] - anterior["temperatura"]) > LIMITES_VARIACAO["temperatura"]:
        score -= PENALIDADES["variacao_brusca"]

    if abs(atual["umidade"] - anterior["umidade"]) > LIMITES_VARIACAO["umidade"]:
        score -= PENALIDADES["variacao_brusca"]

    if abs(atual["pressao"] - anterior["pressao"]) > LIMITES_VARIACAO["pressao"]:
        score -= PENALIDADES["variacao_brusca"]

    if abs(atual["fumaca"] - anterior["fumaca"]) > LIMITES_VARIACAO["fumaca"]:
        score -= PENALIDADES["variacao_brusca"]

    if abs(atual["co"] - anterior["co"]) > LIMITES_VARIACAO["co"]:
        score -= PENALIDADES["variacao_brusca"]

    if abs(atual["pm1"] - anterior["pm1"]) > LIMITES_VARIACAO["pm1"]:
        score -= PENALIDADES["variacao_brusca"]

    if abs(atual["pm25"] - anterior["pm25"]) > LIMITES_VARIACAO["pm25"]:
        score -= PENALIDADES["variacao_brusca"]

    if abs(atual["pm10"] - anterior["pm10"]) > LIMITES_VARIACAO["pm10"]:
        score -= PENALIDADES["variacao_brusca"]

    return max(score, 0)

def calcular_consistencia(linha):

    score = 1.0

    for nome_regra, regra in REGRAS_CONSISTENCIA.items():

        regra_valida = True

        for comparacao in regra["comparacoes"]:

            sensor = comparacao["sensor"]
            operador = comparacao["operador"]

            if operador == ">":

                if not linha[sensor] > comparacao["valor"]:
                    regra_valida = False
                    break

            elif operador == "<":

                if not linha[sensor] < comparacao["valor"]:
                    regra_valida = False
                    break

            elif operador == ">=":

                if not linha[sensor] >= comparacao["valor"]:
                    regra_valida = False
                    break

            elif operador == "<=":

                if not linha[sensor] <= comparacao["valor"]:
                    regra_valida = False
                    break

            elif operador == "==":

                if not linha[sensor] == comparacao["valor"]:
                    regra_valida = False
                    break

            elif operador == "<sensor":

                outro_sensor = comparacao["sensor_ref"]

                if not linha[sensor] < linha[outro_sensor]:
                    regra_valida = False
                    break

            elif operador == ">sensor":

                outro_sensor = comparacao["sensor_ref"]

                if not linha[sensor] > linha[outro_sensor]:
                    regra_valida = False
                    break

        if regra_valida:

            score -= regra["penalidade"]

    return max(score, 0)

# ICA

def calcular_ica(df):

    icas = []

    for indice in range(len(df)):

        linha = df.iloc[indice]

        integridade = calcular_integridade(linha)

        cobertura = calcular_cobertura(linha)

        consistencia = calcular_consistencia(linha)

        estabilidade = calcular_estabilidade(df, indice)

        ica = (

            PESOS_ICA["integridade"] * integridade +

            PESOS_ICA["consistencia"] * consistencia +

            PESOS_ICA["estabilidade"] * estabilidade +

            PESOS_ICA["cobertura"] * cobertura

        )

        icas.append(round(ica, 3))

    df["ICA"] = icas

    return df