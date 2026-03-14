import requests
from books import books

book = input("Digite o nome do livro: ").lower().replace(" ", "")
chapter = input("Digite o número do capítulo: ").strip()
verse = input("Digite o número do versículo: ").strip()

if book not in books:
    print("Livro não encontrado.")
    exit()

url = f"https://bible-api.com/{books[book]}+{chapter}:{verse}?translation=almeida"

resposta = requests.get(url)

if resposta.status_code != 200:
    print("Erro ao conectar com a API.")
    exit()
    
dados = resposta.json()

print("Referência:", dados["reference"])
print("Texto:", dados["text"])