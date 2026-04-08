from google import genai

client = genai.Client(api_key="AIzaSyC2eTBTwODgsGMxGDvIUFKyWaESTAcit-4")

# 🔍 List available models
models = client.models.list()

for m in models:
    print(m.name)