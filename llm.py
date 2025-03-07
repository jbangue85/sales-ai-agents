import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configurar el modelo
model = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0,
    max_tokens=1000,
    verbose=True
)

# Invocar el modelo
response = model.invoke("Write a poem about AI")

# Imprimir solo el contenido generado
print(response.content)
