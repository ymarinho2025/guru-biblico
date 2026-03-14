import requests
from books import books

BASE_URL = "https://bible-api.com"
TRANSLATION = "almeida"
TIMEOUT = 20

sucesso = []
erro_conexao = []
erro_api = []

print("Iniciando testes dos livros...\n")

for chave_pt, nome_api in books.items():
    chapter = "1"
    verse = "1"
    url = f"{BASE_URL}/{nome_api}+{chapter}:{verse}?translation={TRANSLATION}"

    try:
        resposta = requests.get(url, timeout=TIMEOUT)
    except requests.exceptions.RequestException as e:
        erro_conexao.append({
            "livro_digitado": chave_pt,
            "livro_api": nome_api,
            "url": url,
            "erro": str(e)
        })
        print(f"[ERRO CONEXAO] {chave_pt} -> {nome_api}")
        continue

    if resposta.status_code != 200:
        erro_conexao.append({
            "livro_digitado": chave_pt,
            "livro_api": nome_api,
            "url": url,
            "erro": f"HTTP {resposta.status_code}"
        })
        print(f"[ERRO HTTP] {chave_pt} -> {nome_api} | HTTP {resposta.status_code}")
        continue

    try:
        dados = resposta.json()
    except ValueError:
        erro_api.append({
            "livro_digitado": chave_pt,
            "livro_api": nome_api,
            "url": url,
            "erro": "Resposta não é JSON válido"
        })
        print(f"[ERRO API] {chave_pt} -> {nome_api} | JSON inválido")
        continue

    if "reference" in dados and "text" in dados:
        sucesso.append({
            "livro_digitado": chave_pt,
            "livro_api": nome_api,
            "reference": dados["reference"]
        })
        print(f"[OK] {chave_pt} -> {nome_api} | {dados['reference']}")
    else:
        mensagem_erro = dados.get("error", "Resposta sem 'reference' e sem 'text'")
        erro_api.append({
            "livro_digitado": chave_pt,
            "livro_api": nome_api,
            "url": url,
            "erro": mensagem_erro,
            "resposta": dados
        })
        print(f"[ERRO API] {chave_pt} -> {nome_api} | {mensagem_erro}")

print("\n" + "=" * 60)
print("RESUMO FINAL")
print("=" * 60)

print(f"\nTotal com sucesso: {len(sucesso)}")
for item in sucesso:
    print(f"  - {item['livro_digitado']} -> {item['livro_api']} | {item['reference']}")

print(f"\nTotal com erro de conexão/HTTP: {len(erro_conexao)}")
for item in erro_conexao:
    print(f"  - {item['livro_digitado']} -> {item['livro_api']}")
    print(f"    URL: {item['url']}")
    print(f"    Erro: {item['erro']}")

print(f"\nTotal com erro de resposta da API: {len(erro_api)}")
for item in erro_api:
    print(f"  - {item['livro_digitado']} -> {item['livro_api']}")
    print(f"    URL: {item['url']}")
    print(f"    Erro: {item['erro']}")
