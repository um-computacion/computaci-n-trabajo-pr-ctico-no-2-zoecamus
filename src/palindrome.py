def is_palindrome(word: str):
    word = word.replace(" ", "").lower()
    return word == word[::-1]   

def get_input():
    word = input("Ingrese una palabra o frase: ")
    if word == "":
        print("Entrada vacía. Intente nuevamente.")
        return get_input() 
    return word

word = get_input()
if is_palindrome(word):
    print(f"'{word}' es un palíndromo.")
else:
    print(f"'{word}' no es un palíndromo.")