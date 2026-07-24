#Configurações do Índice de Confiabilidade Ambiental (ICA)
#Este arquivo contém todas as regras utilizadas para
#avaliar a qualidade dos dados ambientais.
# PESOS DO ICA

PESOS_ICA = {

    "integridade": 0.30,

    "consistencia": 0.35,

    "estabilidade": 0.20,

    "cobertura": 0.15

}
# PENALIDADES

PENALIDADES = {

    "valor_nulo": 0.20,

    "valor_extremo": 0.15,

    "variacao_brusca": 0.10,

    "inconsistencia": 0.10

}
# VARIAÇÃO MÁXIMA ENTRE DUAS LEITURAS
# (considerando intervalo de aproximadamente 20 segundos)

LIMITES_VARIACAO = {

    "temperatura": 2.0,

    "umidade": 8.0,

    "pressao": 3.0,

    "fumaca": 80,

    "co": 5,

    "pm1": 15,

    "pm25": 20,

    "pm10": 25

}

# REGRAS DE CONSISTÊNCIA FÍSICA


REGRAS_CONSISTENCIA = {

    "co_alto_sem_fumaca": {

        "descricao":
            "CO elevado normalmente acompanha aumento de fumaça.",

        "condicao": {

            "co_min": 15,

            "fumaca_max": 180

        },

        "penalidade": 0.15

    },

    "pm25_alto_sem_fumaca": {

        "descricao":
            "PM2.5 muito alto sem aumento de fumaça pode indicar inconsistência.",

        "condicao": {

            "pm25_min": 60,

            "fumaca_max": 180

        },

        "penalidade": 0.10

    },

    "temperatura_alta_umidade_alta": {

        "descricao":
            "Temperaturas muito elevadas geralmente reduzem a umidade relativa.",

        "condicao": {

            "temperatura_min": 38,

            "umidade_min": 85

        },

        "penalidade": 0.10

    },

    "pm10_menor_pm25": {

        "descricao":
            "PM10 não deve ser menor que PM2.5.",

        "penalidade": 0.20

    }

}
# CLASSIFICAÇÃO DO ICA

CLASSIFICACAO_ICA = {

    "excelente": (0.95, 1.00),

    "boa": (0.85, 0.95),

    "aceitavel": (0.70, 0.85),

    "baixa": (0.50, 0.70),

    "critica": (0.00, 0.50)

}
# CONFIGURAÇÕES GERAIS

CONFIG_ICA = {

    "valor_maximo": 1.0,

    "valor_minimo": 0.0,

    "usar_penalizacao_progressiva": True,

    "arredondamento": 3

}

RISCOS_AMBIENTAIS = {

    "temperatura":{

        "tendencia":"subir"

    },

    "umidade":{

        "tendencia":"descer"

    },

    "fumaca":{

        "tendencia":"subir"

    },

    "co":{

        "tendencia":"subir"

    },

    "pm25":{

        "tendencia":"subir"

    },

    "pm10":{

        "tendencia":"subir"

    }

}

RELACOES_SENSORES = {

    "temperatura": [

        "umidade",

        "fumaca"

    ],

    "fumaca": [

        "co",

        "pm25",

        "pm10"

    ],

    "co": [

        "fumaca"

    ],

    "pm25": [

        "fumaca",

        "pm10"

    ]

}

REGRAS_CONSISTENCIA = {

    "co_alto_sem_fumaca": {

        "descricao": "CO elevado normalmente acompanha aumento de fumaça.",

        "comparacoes": [

            {
                "sensor": "co",
                "operador": ">",
                "valor": 15
            },

            {
                "sensor": "fumaca",
                "operador": "<",
                "valor": 180
            }

        ],

        "penalidade": 0.15

    },

    "pm25_alto_sem_fumaca": {

        "descricao": "PM2.5 muito alto sem fumaça.",

        "comparacoes": [

            {
                "sensor": "pm25",
                "operador": ">",
                "valor": 60
            },

            {
                "sensor": "fumaca",
                "operador": "<",
                "valor": 180
            }

        ],

        "penalidade": 0.10

    },

    "temperatura_alta_umidade_alta": {

        "descricao": "Temperatura muito alta junto com umidade alta.",

        "comparacoes": [

            {
                "sensor": "temperatura",
                "operador": ">",
                "valor": 38
            },

            {
                "sensor": "umidade",
                "operador": ">",
                "valor": 85
            }

        ],

        "penalidade": 0.10

    },

    "pm10_menor_pm25": {

        "descricao": "PM10 não deve ser menor que PM2.5.",

        "comparacoes": [

            {
                "sensor": "pm10",
                "operador": "<sensor",
                "sensor_ref": "pm25"
            }

        ],

        "penalidade": 0.20

    }
}
PESOS_MEMORIA = {

    "curta":0.50,

    "media":0.30,

    "longa":0.20

}