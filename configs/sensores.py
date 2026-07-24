#config.py
#Configurações centrais do projeto IGNIS
#limites físicos, limites ambientais, pesos da IA e metadados.
#descreve todos os sensore para a ia


SENSORES = {

    "temperatura": {

        # Informações gerais
        "nome": "Temperatura do Ar",
        "descricao": "Temperatura ambiente medida pelo BME280.",
        "sensor": "BME280",
        "categoria": "Meteorologia",
        "tipo": "Climático",

        "unidade": "°C",

        # Faixa utilizada pelo modelo
        "min": 10,
        "max": 50,

        # Faixas ambientais
        "ideal": (18,28),
        "atencao": (28,35),
        "alerta": (35,40),
        "critico": (40,50),

        # IA 
        "peso": 0.20,

        "participa_features":[

            "indice_secura",

            "variacao_temperatura",

            "media_temperatura",

            "tendencia_temperatura"

        ],

        "impactos":[

            "propagacao_fogo",

            "ressecamento",

            "aumento_risco"

        ],

        "direcao_risco":"maior_valor_maior_risco",

        "usar_normalizacao":True,

        "usar_media_movel":True,

        "usar_delta":True,

        "usar_eai":True,

        #memoria
        "limiar_memoria": 0.70,

        "janela_memoria": {

            "curta":5,
            "media":10,
            "longa":20 
        }

    },

    ##################################################################

    "umidade":{

        "nome":"Umidade Relativa",

        "descricao":"Umidade relativa do ar medida pelo BME280.",

        "sensor":"BME280",

        "categoria":"Meteorologia",

        "tipo":"Climático",

        "unidade":"%",

        "min":10,

        "max":100,

        "ideal":(50,70),

        "atencao":(35,50),

        "alerta":(20,35),

        "critico":(10,20),

        "peso":0.22,

        "participa_features":[

            "indice_secura",

            "variacao_umidade",

            "media_umidade"

        ],

        "impactos":[

            "ressecamento",

            "propagacao_fogo"

        ],

        "direcao_risco":"menor_valor_maior_risco",

        "usar_normalizacao":True,

        "usar_media_movel":True,

        "usar_delta":True,

        "usar_eai":True,

         #memoria
        "limiar_memoria": 0.30,

        "janela_memoria": {
    "curta": 5,
    "media": 10,
    "longa": 20
}

    },

    ##################################################################

    "pressao":{

        "nome":"Pressão Atmosférica",

        "descricao":"Pressão atmosférica medida pelo BME280.",

        "sensor":"BME280",

        "categoria":"Meteorologia",

        "tipo":"Climático",

        "unidade":"hPa",

        "min":950,

        "max":1050,

        "ideal":(1008,1018),

        "atencao":(1000,1008),

        "alerta":(990,1000),

        "critico":(950,990),

        "peso":0.05,

        "participa_features":[

            "indice_estabilidade",

            "media_pressao"

        ],

        "impactos":[

            "estabilidade_atmosferica"

        ],

        "direcao_risco":"variavel",

        "usar_normalizacao":True,

        "usar_media_movel":True,

        "usar_delta":False,

        "usar_eai":False,

         #memoria
        "limiar_memoria": 0.50,

        "limiar_memoria": 0.50,

"janela_memoria": {
    "curta": 10,
    "media": 20,
    "longa": 40
}

    },

    ##################################################################

    "fumaca":{

        "nome":"Fumaça",

        "descricao":"Concentração relativa detectada pelo MQ2.",

        "sensor":"MQ2",

        "categoria":"Qualidade do Ar",

        "tipo":"Poluição",

        "unidade":"ADC",

        "min":150,

        "max":800,

        "ideal":(150,250),

        "atencao":(250,350),

        "alerta":(350,500),

        "critico":(500,800),

        "peso":0.18,

        "participa_features":[

            "indice_poluicao",

            "indice_combustao",

            "variacao_fumaca"

        ],

        "impactos":[

            "combustao",

            "queimada",

            "qualidade_ar"

        ],

        "direcao_risco":"maior_valor_maior_risco",

        "usar_normalizacao":True,

        "usar_media_movel":True,

        "usar_delta":True,

        "usar_eai":True,

         #memoria
        "limiar_memoria": 0.55,

        "limiar_memoria": 0.55,

"janela_memoria": {
    "curta": 3,
    "media": 8,
    "longa": 15
}

    },

    ##################################################################

    "co":{

        "nome":"Monóxido de Carbono",

        "descricao":"Concentração estimada de CO detectada pelo MQ7.",

        "sensor":"MQ7",

        "categoria":"Gases",

        "tipo":"Poluição",

        "unidade":"ppm",

        "min":0,

        "max":50,

        "ideal":(0,5),

        "atencao":(5,10),

        "alerta":(10,20),

        "critico":(20,50),

        "peso":0.18,

        "participa_features":[

            "indice_poluicao",

            "indice_combustao",

            "relacao_co_fumaca",

            "variacao_co"

        ],

        "impactos":[

            "combustao",

            "qualidade_ar",

            "toxicidade"

        ],

        "direcao_risco":"maior_valor_maior_risco",

        "usar_normalizacao":True,

        "usar_media_movel":True,

        "usar_delta":True,

        "usar_eai":True,

         #memoria
        "limiar_memoria": 0.45,

        "limiar_memoria": 0.45,

"janela_memoria": {
    "curta": 5,
    "media": 12,
    "longa": 25
}

    },

    ##################################################################

    "pm1":{

        "nome":"PM1",

        "descricao":"Material particulado menor que 1µm.",

        "sensor":"PMS7003",

        "categoria":"Material Particulado",

        "tipo":"Poluição",

        "unidade":"µg/m³",

        "min":0,

        "max":100,

        "ideal":(0,10),

        "atencao":(10,25),

        "alerta":(25,50),

        "critico":(50,100),

        "peso":0.05,

        "participa_features":[

            "indice_poluicao"

        ],

        "impactos":[

            "qualidade_ar"

        ],

        "direcao_risco":"maior_valor_maior_risco",

        "usar_normalizacao":True,

        "usar_media_movel":True,

        "usar_delta":True,

        "usar_eai":False,

         #memoria
        "limiar_memoria": 0.50,

        "janela_memoria": {
    "curta": 3,
    "media": 6,
    "longa": 12
}

    },

    ##################################################################

    "pm25":{

        "nome":"PM2.5",

        "descricao":"Material particulado fino.",

        "sensor":"PMS7003",

        "categoria":"Material Particulado",

        "tipo":"Poluição",

        "unidade":"µg/m³",

        "min":0,

        "max":150,

        "ideal":(0,15),

        "atencao":(15,35),

        "alerta":(35,75),

        "critico":(75,150),

        "peso":0.22,

        "participa_features":[

            "indice_poluicao",

            "relacao_pm",

            "variacao_pm25"

        ],

        "impactos":[

            "qualidade_ar",

            "combustao"

        ],

        "direcao_risco":"maior_valor_maior_risco",

        "usar_normalizacao":True,

        "usar_media_movel":True,

        "usar_delta":True,

        "usar_eai":True,

         #memoria
        "limiar_memoria": 0.60,

"janela_memoria": {
    "curta": 4,
    "media": 10,
    "longa": 20
}

    },

    ##################################################################

    "pm10":{

        "nome":"PM10",

        "descricao":"Material particulado inalável.",

        "sensor":"PMS7003",

        "categoria":"Material Particulado",

        "tipo":"Poluição",

        "unidade":"µg/m³",

        "min":0,

        "max":200,

        "ideal":(0,25),

        "atencao":(25,50),

        "alerta":(50,100),

        "critico":(100,200),

        "peso":0.15,

        "participa_features":[

            "indice_poluicao",

            "relacao_pm",

            "variacao_pm10"

        ],

        "impactos":[

            "qualidade_ar",

            "combustao"

        ],

        "direcao_risco":"maior_valor_maior_risco",

        "usar_normalizacao":True,

        "usar_media_movel":True,

        "usar_delta":True,

        "usar_eai":False,

         #memoria
        "limiar_memoria": 0.55,

        "janela_memoria": {
    "curta": 6,
    "media": 15,
    "longa": 30
}

    }

}
