#controla o treinamento
# Janelas temporais
JANELA_CURTA = 5
JANELA_MEDIA = 10
JANELA_LONGA = 20
#Janela que a ia vai usar
TAMANHO_JANELA = JANELA_MEDIA

# Horizonte de previsão (quantas leituras à frente)
HORIZONTE_PREVISAO = 5

#Variável alvo
ALVO = "EAI"

#Dataset
# Quantidade mínima de registros para iniciar o treinamento
TESTE = 0.20
MIN_REGISTROS = 100

# Tamanho do lote (batch)
BATCH_SIZE = 32

# Número de épocas
EPOCHS = 100

# Taxa de aprendizado
LEARNING_RATE = 0.001

# Seed para reprodutibilidade
RANDOM_STATE = 42

# Tipo do modelo

TIPO_MODELO = "regressao"

# Variável prevista

ALVO = "EAI"

# Horizonte

HORIZONTE_PREVISAO = 5

# Sensores usados no modo multivariado

SENSORES_PREVISAO = [

    "temperatura",

    "umidade",

    "fumaca",

    "co",

    "pm25"
]

# Limiar para classificação

LIMIAR_RISCO = 0.70





LSTM_UNITS = 64

DROPOUT = 0.20

RECURRENT_DROPOUT = 0.10

CAMADAS_LSTM = 2




#Para experimentos
# Early Stopping
PATIENCE = 15

# Salvar melhor modelo
SALVAR_MELHOR_MODELO = True

# Caminho do modelo
MODELO_PATH = "models/lstm.keras"
