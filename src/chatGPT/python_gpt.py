import openai
# Inicializar la API key de OpenAI
openai.api_key = "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"
# Configuración del modelo de chat
TOP_P = 1
FREQ_PENALTY = 0
PRES_PENALTY = 0
STOP = None
MAX_TOKENS = 1024
TEMPERATURE = 0.75
NMAX = 1
MODEL_ENGINE = "text-davinci-003"

# Solicitar una consulta al usuario
user_query = input("Por favor, ingrese su consulta: ")

# Verificar si la consulta tiene contenido
if user_query:
    # Agregar "You:" antes de imprimir y enviar la consulta
    print("You:", user_query)

    # Invocar el modelo de chat de OpenAI con la consulta del usuario
    completion = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=user_query,
        max_tokens=MAX_TOKENS,
        n=NMAX,
        top_p=TOP_P,
        frequency_penalty=FREQ_PENALTY,
        presence_penalty=PRES_PENALTY,
        temperature=TEMPERATURE,
        stop=STOP
    )
    # Obtener la respuesta del modelo de chat
    response = completion.choices[0].text.strip()
    # Agregar "chatGPT:" antes de imprimir la respuesta del modelo de chat
    print("chatGPT:", response)
else:
    print("Por favor, ingrese una consulta válida.")
