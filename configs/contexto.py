"""
contexto.py
Configurações do Modelo de Contexto Ambiental do IGNIS.
Todos os pesos utilizados nas features de contexto
são centralizados aqui para facilitar calibração,
testes científicos e futuras publicações.
"""

#analisa eventos externos
# ESTADO CLIMÁTICO

PESOS_ESTADO_CLIMATICO = {

    "temperatura": 0.45,
    "umidade": 0.35,
    "pressao": 0.20

}

# ESTADO DA COMBUSTÃO

PESOS_ESTADO_COMBUSTAO = {

    "fumaca": 0.50,
    "co": 0.35,
    "pm25": 0.15

}

# ESTADO DA POLUIÇÃO
PESOS_ESTADO_POLUICAO = {

    "pm1": 0.20,
    "pm25": 0.40,
    "pm10": 0.20,
    "co": 0.20

}
# ESTADO DE SECURA
PESOS_ESTADO_SECURA = {

    "indice_secura": 0.70,
    "indice_termico": 0.30

}

# CONTEXTO ATMOSFÉRICO
PESOS_CONTEXTO_ATMOSFERICO = {

    "indice_atmosferico": 0.60,
    "estado_climatico": 0.40

}

# CONTEXTO AMBIENTAL GLOBAL
PESOS_CONTEXTO_GLOBAL = {

    "estado_climatico": 0.25,
    "estado_combustao": 0.25,
    "estado_poluicao": 0.20,
    "estado_secura": 0.15,
    "contexto_atmosferico": 0.15

}

# MEMÓRIA DO CONTEXTO
JANELA_MEMORIA_CONTEXTO = {

    "curta": 5,
    "media": 10,
    "longa": 20

}

# TENDÊNCIA

JANELA_TENDENCIA = 5

# LIMIARES
LIMIAR_CONTEXTO_ESTAVEL = 0.30
LIMIAR_CONTEXTO_ATENCAO = 0.50
LIMIAR_CONTEXTO_ALERTA = 0.70

# PERSISTÊNCIA

LIMIAR_PERSISTENCIA = 0.70

# SEVERIDADE

FATOR_SEVERIDADE = 10

# CLASSES AMBIENTAIS


CLASSES_CONTEXTO = {

    "estavel": "Estável",
    "atencao": "Atenção",
    "alerta": "Alerta",
    "critico": "Crítico"

}