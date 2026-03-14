from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

referencia = os.getenv("VERSE_REFERENCE")
texto = os.getenv("VERSE_TEXT")

modelo = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    api_key=os.getenv("API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

mensagens = [
    SystemMessage(
        content="Você é um professor de Bíblia. Crie um estudo bíblico profundo e claro em português."
    ),
    HumanMessage(
        content=f"Crie um estudo bíblico baseado no versículo:\n{referencia}\n\n{texto}"
    ),
]

resposta = modelo.invoke(mensagens)

print("\n===== ESTUDO BÍBLICO PERSONALIZADO =====\n")
print(resposta.content)