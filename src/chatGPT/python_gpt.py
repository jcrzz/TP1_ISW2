#!/usr/bin/python 
import openai 
import argparse
# configuración de argumentos de línea de comando
parser = argparse.ArgumentParser(description='Programa de chat con GPT-3')
parser.add_argument('--convers', action='store_true', help='Habilita el modo de conversación')
args = parser.parse_args()
# inicialización de la API de OpenAI
openai.api_key = "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"
# parámetros de la API
TOP_P=1          
FREQ_PENALTY=0          
PRES_PENALTY=0          
STOP=None 
MAX_TOKENS=1024 
TEMPERATURE=0.75 
NMAX=1 
MODEL_ENGINE = "text-davinci-003" 
# buffer para almacenar las consultas y respuestas anteriores
conversation_buffer = []
# función para imprimir el contenido de la consulta o la respuesta
def print_message(message, is_user_message=True):
    prefix = "You: " if is_user_message else "chatGPT: "
    print(prefix + message)
# bucle principal para el modo de conversación
while args.convers:
    # aceptar consulta del usuario
    user_input = input("Ingrese su consulta: ")
    # si la consulta es nula, se ignora y se vuelve a pedir
    if not user_input:
        continue
    # salir del modo conversación al ingresar "salir"
    if user_input == "salir":
        break
    # agregar la consulta al buffer de conversación
    conversation_buffer.append("You: " + user_input)
    # combinar las consultas anteriores con la última para enviar a la API
    prompt = "\n".join(conversation_buffer)
    try:
        # invocar la API de chatGPT con la consulta actual y el buffer completo
        completion = openai.Completion.create(
            engine=MODEL_ENGINE,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            n=NMAX,
            top_p=TOP_P,
            frequency_penalty=FREQ_PENALTY,
            presence_penalty=PRES_PENALTY,
            temperature=TEMPERATURE,
            stop=["You:", "chatGPT:"] # indicar la cadena de STOP para el modo de conversación
        )
        # agregar la respuesta al buffer de conversación
        response = completion.choices[0].text.strip()
        conversation_buffer.append("chatGPT: " + response)
        # imprimir la respuesta de chatGPT
        print_message(response, False)
    except Exception as e:
        # imprimir mensaje de error en caso de excepción
        print("Se produjo un error:", e)