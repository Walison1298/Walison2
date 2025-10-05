# test_gemini.py
import os
from google import genai

# Teste simples para validar a API do Gemini
api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    print("❌ ERRO: Variável GENAI_API_KEY não encontrada. Verifique seu .env ou exportação.")
    exit(1)

try:
    client = genai.Client()
    print("✅ Cliente Gemini inicializado com sucesso!")
except Exception as e:
    print("❌ Erro ao inicializar o cliente:", e)
    exit(1)

try:
    prompt = "Diga olá, mundo, usando o modelo Gemini!"
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        contents=prompt
    )
    print("✅ Resposta do modelo:")
    print(response.text)
except Exception as e:
    print("❌ Erro ao chamar o modelo:", e)
