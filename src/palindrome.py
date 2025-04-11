def limpiar_texto(texto_original):
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "Á": "a", "É": "e", "Í": "i", "Ó": "o", "Ú": "u",
        ".": "", ",": "", "!": "", "?": "", "¿": "", "¡": "", ":": "", ";": ""
    }
    texto_limpio = texto_original.lower().replace(" ", "")
    for caracter, reemplazo in reemplazos.items():
        texto_limpio = texto_limpio.replace(caracter, reemplazo)
    return texto_limpio

def is_palindrome(word: str):
    word = limpiar_texto(word)
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True

def get_input():
    word = input("Ingrese una palabra o frase: ")
    if word == "":
        print("Entrada vacía. Intente nuevamente.")
        return get_input() 
    return word

while True:
    palabra = get_input()
    if palabra.lower() == "exit":
        break
    if is_palindrome(palabra):
        print(f"'{palabra}' es un palíndromo.")
    else:
        print(f"'{palabra}' no es un palíndromo.")



