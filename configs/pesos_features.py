"""
pesos_features.py

Configuração central das features utilizadas pela IA.
"""
#descreve os sensores para as features

FEATURES = {

    # ======================================================
    # Sensores normalizados
    # ======================================================

    "temperatura_norm": {

        "peso": 1.00,
        "usar": True,
        "grupo": "sensores",
        "descricao": "Temperatura normalizada"

    },

    "umidade_norm": {

        "peso": 1.00,
        "usar": True,
        "grupo": "sensores",
        "descricao": "Umidade normalizada"

    },

    "pressao_norm": {

        "peso": 0.80,
        "usar": True,
        "grupo": "sensores",
        "descricao": "Pressão normalizada"

    },

    "fumaca_norm": {

        "peso": 1.20,
        "usar": True,
        "grupo": "sensores",
        "descricao": "Fumaça normalizada"

    },

    "co_norm": {

        "peso": 1.20,
        "usar": True,
        "grupo": "sensores",
        "descricao": "CO normalizado"

    },

    "pm1_norm": {

        "peso": 0.80,
        "usar": True,
        "grupo": "sensores",
        "descricao": "PM1 normalizado"

    },

    "pm25_norm": {

        "peso": 1.30,
        "usar": True,
        "grupo": "sensores",
        "descricao": "PM2.5 normalizado"

    },

    "pm10_norm": {

        "peso": 1.00,
        "usar": True,
        "grupo": "sensores",
        "descricao": "PM10 normalizado"

    },


    
# ======================================================
# B1 - Ambientais
# ======================================================


    "indice_secura":{

        "peso":1.40,
        "usar":True,
        "grupo":"ambientais"

},

"indice_poluicao":{

    "peso":1.50,
    "usar":True,
    "grupo":"ambientais"

},

"indice_combustao":{

    "peso":1.80,
    "usar":True,
    "grupo":"ambientais"

},

"indice_particulas":{

    "peso":1.20,
    "usar":True,
    "grupo":"ambientais"

},

"indice_termico":{

    "peso":1.10,
    "usar":True,
    "grupo":"ambientais"

},

"indice_atmosferico":{

    "peso":0.80,
    "usar":True,
    "grupo":"ambientais"

},
"indice_risco":{

    "peso":2.00,
    "usar":True,
    "grupo":"ambientais"

},

"indice_estabilidade":{

    "peso":1.50,
    "usar":True,
    "grupo":"ambientais"

},


# ======================================================
# B3 - Dinâmica Temporal
# ======================================================

# Temperatura
"delta_temperatura": {"peso": 1.30, "usar": True, "grupo": "dinamica"},
"intensidade_temperatura": {"peso": 1.20, "usar": True, "grupo": "dinamica"},
"direcao_temperatura": {"peso": 0.80, "usar": True, "grupo": "dinamica"},
"aceleracao_temperatura": {"peso": 1.20, "usar": True, "grupo": "dinamica"},

# Umidade
"delta_umidade": {"peso": 1.30, "usar": True, "grupo": "dinamica"},
"intensidade_umidade": {"peso": 1.20, "usar": True, "grupo": "dinamica"},
"direcao_umidade": {"peso": 0.80, "usar": True, "grupo": "dinamica"},
"aceleracao_umidade": {"peso": 1.20, "usar": True, "grupo": "dinamica"},

# Pressão
"delta_pressao": {"peso": 0.90, "usar": True, "grupo": "dinamica"},
"intensidade_pressao": {"peso": 0.80, "usar": True, "grupo": "dinamica"},
"direcao_pressao": {"peso": 0.60, "usar": True, "grupo": "dinamica"},
"aceleracao_pressao": {"peso": 0.80, "usar": True, "grupo": "dinamica"},

# Fumaça
"delta_fumaca": {"peso": 1.50, "usar": True, "grupo": "dinamica"},
"intensidade_fumaca": {"peso": 1.40, "usar": True, "grupo": "dinamica"},
"direcao_fumaca": {"peso": 1.00, "usar": True, "grupo": "dinamica"},
"aceleracao_fumaca": {"peso": 1.40, "usar": True, "grupo": "dinamica"},

# CO
"delta_co": {"peso": 1.50, "usar": True, "grupo": "dinamica"},
"intensidade_co": {"peso": 1.40, "usar": True, "grupo": "dinamica"},
"direcao_co": {"peso": 1.00, "usar": True, "grupo": "dinamica"},
"aceleracao_co": {"peso": 1.40, "usar": True, "grupo": "dinamica"},

# PM1
"delta_pm1": {"peso": 1.10, "usar": True, "grupo": "dinamica"},
"intensidade_pm1": {"peso": 1.00, "usar": True, "grupo": "dinamica"},
"direcao_pm1": {"peso": 0.80, "usar": True, "grupo": "dinamica"},
"aceleracao_pm1": {"peso": 1.00, "usar": True, "grupo": "dinamica"},

# PM2.5
"delta_pm25": {"peso": 1.60, "usar": True, "grupo": "dinamica"},
"intensidade_pm25": {"peso": 1.50, "usar": True, "grupo": "dinamica"},
"direcao_pm25": {"peso": 1.10, "usar": True, "grupo": "dinamica"},
"aceleracao_pm25": {"peso": 1.50, "usar": True, "grupo": "dinamica"},

# PM10
"delta_pm10": {"peso": 1.40, "usar": True, "grupo": "dinamica"},
"intensidade_pm10": {"peso": 1.30, "usar": True, "grupo": "dinamica"},
"direcao_pm10": {"peso": 1.00, "usar": True, "grupo": "dinamica"},
"aceleracao_pm10": {"peso": 1.30, "usar": True, "grupo": "dinamica"},

# ======================================================
# B6 - Memória Temporal
# ======================================================

# Temperatura
"memoria_curta_temperatura": {"peso": 1.40, "usar": True, "grupo": "memoria"},
"memoria_media_temperatura": {"peso": 1.50, "usar": True, "grupo": "memoria"},
"memoria_longa_temperatura": {"peso": 1.60, "usar": True, "grupo": "memoria"},
"persistencia_temperatura": {"peso": 1.70, "usar": True, "grupo": "memoria"},

# Umidade
"memoria_curta_umidade": {"peso": 1.40, "usar": True, "grupo": "memoria"},
"memoria_media_umidade": {"peso": 1.50, "usar": True, "grupo": "memoria"},
"memoria_longa_umidade": {"peso": 1.60, "usar": True, "grupo": "memoria"},
"persistencia_umidade": {"peso": 1.70, "usar": True, "grupo": "memoria"},

# Pressão
"memoria_curta_pressao": {"peso": 1.00, "usar": True, "grupo": "memoria"},
"memoria_media_pressao": {"peso": 1.10, "usar": True, "grupo": "memoria"},
"memoria_longa_pressao": {"peso": 1.20, "usar": True, "grupo": "memoria"},
"persistencia_pressao": {"peso": 1.20, "usar": True, "grupo": "memoria"},

# Fumaça
"memoria_curta_fumaca": {"peso": 1.80, "usar": True, "grupo": "memoria"},
"memoria_media_fumaca": {"peso": 1.90, "usar": True, "grupo": "memoria"},
"memoria_longa_fumaca": {"peso": 2.00, "usar": True, "grupo": "memoria"},
"persistencia_fumaca": {"peso": 2.20, "usar": True, "grupo": "memoria"},

# CO
"memoria_curta_co": {"peso": 1.80, "usar": True, "grupo": "memoria"},
"memoria_media_co": {"peso": 1.90, "usar": True, "grupo": "memoria"},
"memoria_longa_co": {"peso": 2.00, "usar": True, "grupo": "memoria"},
"persistencia_co": {"peso": 2.20, "usar": True, "grupo": "memoria"},

# PM1
"memoria_curta_pm1": {"peso": 1.20, "usar": True, "grupo": "memoria"},
"memoria_media_pm1": {"peso": 1.30, "usar": True, "grupo": "memoria"},
"memoria_longa_pm1": {"peso": 1.40, "usar": True, "grupo": "memoria"},
"persistencia_pm1": {"peso": 1.50, "usar": True, "grupo": "memoria"},

# PM2.5
"memoria_curta_pm25": {"peso": 2.00, "usar": True, "grupo": "memoria"},
"memoria_media_pm25": {"peso": 2.10, "usar": True, "grupo": "memoria"},
"memoria_longa_pm25": {"peso": 2.20, "usar": True, "grupo": "memoria"},
"persistencia_pm25": {"peso": 2.40, "usar": True, "grupo": "memoria"},

# PM10
"memoria_curta_pm10": {"peso": 1.70, "usar": True, "grupo": "memoria"},
"memoria_media_pm10": {"peso": 1.80, "usar": True, "grupo": "memoria"},
"memoria_longa_pm10": {"peso": 1.90, "usar": True, "grupo": "memoria"},
"persistencia_pm10": {"peso": 2.10, "usar": True, "grupo": "memoria"},

# ======================================================
# B7 - Contexto Ambiental
# ======================================================

"contexto_hora": {
    "peso": 0.80,
    "usar": True,
    "grupo": "contexto"
},

"contexto_mes": {
    "peso": 0.70,
    "usar": True,
    "grupo": "contexto"
},

"contexto_estacao": {
    "peso": 1.00,
    "usar": True,
    "grupo": "contexto"
},

"contexto_periodo_seco": {
    "peso": 1.50,
    "usar": True,
    "grupo": "contexto"
},

"contexto_periodo_chuvoso": {
    "peso": 1.30,
    "usar": True,
    "grupo": "contexto"
},

"contexto_fim_semana": {
    "peso": 0.50,
    "usar": True,
    "grupo": "contexto"
},

"contexto_dia_ano": {
    "peso": 0.70,
    "usar": True,
    "grupo": "contexto"
},

"contexto_epoca_critica": {
    "peso": 1.80,
    "usar": True,
    "grupo": "contexto"
},

# ======================================================
# Estado Ambiental Integrado (EAI)
# ======================================================

"EAI": {
    "peso": 3.00,
    "usar": True,
    "grupo": "eai"
},

"EAI_persistencia": {
    "peso": 2.60,
    "usar": True,
    "grupo": "eai"
},

"EAI_tendencia": {
    "peso": 2.20,
    "usar": True,
    "grupo": "eai"
},

"EAI_velocidade": {
    "peso": 2.10,
    "usar": True,
    "grupo": "eai"
},

"EAI_direcao": {
    "peso": 1.40,
    "usar": True,
    "grupo": "eai"
},

"EAI_intensidade": {
    "peso": 2.00,
    "usar": True,
    "grupo": "eai"
},

"EAI_aceleracao": {
    "peso": 2.10,
    "usar": True,
    "grupo": "eai"
},

"EAI_severidade": {
    "peso": 3.20,
    "usar": True,
    "grupo": "eai"
}
}