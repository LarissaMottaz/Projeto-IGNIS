# coleta de dados do ThingSpeak
#importa os dados da plataforma em nuven
import requests
import pandas as pd

CHANNEL_ID = "3311594"
READ_API_KEY = "XTI6H9M0VBFM5NYL"

URL = (
    f"https://api.thingspeak.com/channels/{3311594}"
    f"/feeds.json?api_key={READ_API_KEY}&results=500"
)


def obter_dados():

    resposta = requests.get(URL)

    dados = resposta.json()["feeds"]

    df = pd.DataFrame(dados)

    return df