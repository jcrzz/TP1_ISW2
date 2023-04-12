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

while True:
    try:
        # Aceptar una consulta del usuario
        user_query = input("Por favor, ingrese su consulta (o 'q' para salir): ")

        # Salir si el usuario ingresa 'q'
        if user_query == 'q':
            break

        # Verificar si la consulta tiene contenido
        if not user_query:
            raise ValueError("La consulta no puede estar vacía")

        try:
            # Tratar la consulta
            prompt = "You: " + user_query

            # Invocar el modelo de chat de OpenAI con la consulta del usuario
            completion = openai.Completion.create(
                engine=MODEL_ENGINE,
                prompt=prompt,
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

            try:
                # Imprimir la respuesta del modelo de chat
                print("chatGPT:", response)

            except Exception as e:
                print("Ha ocurrido un error al imprimir la respuesta:", e)

        except Exception as e:
            print("Ha ocurrido un error al invocar el modelo de chat:", e)

    except Exception as e:
        print("Ha ocurrido un error:", e)
