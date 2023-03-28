import random

# inicializo la cantidad de vidas según nivel de dificultad
difficulty = int(input('Seleccioná el nivel de dificultad (escribí 1, 2 o 3):\n'
                       '1 Fácil\n2 Normal\n3 Difícil\n '))
if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
if difficulty == 3:
    lives = 5

# leo el archivo con las palabras
with open('words.txt', 'r') as fetch:
    words = fetch.read().split(',')

# sorteo una palabra de la lista
secret_word = random.choice(words)

# creo la pista según la palabra sorteada
clue = []
for i in range(0, len(secret_word)):
    clue.append('?')

heart_symbol = u'\u2764'
# cuento cantidad de letras
unknown_letters = len(secret_word)

# defino el estado del juego
guessed_word_correctly = False


# función para actualizar la pista
def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknown_letters -= 1
        index += 1
    return unknown_letters


# controlo el ciclo del juego
while lives > 0:
    print(clue)
    print(f'Vidas restantes: {heart_symbol * lives}')
    guess = input('Adiviná una letra o la palabra: ').lower()

    # ¿adivinó la palabra completa?
    if guess == secret_word:
        guessed_word_correctly = True
        break

    # ¿adivinó alguna letra de la palabra?
    if guess in secret_word:
        unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
    else:
        print('Incorrecto. Perdés una vida...')
        lives -= 1

    # ¿se adivinaron todas las letras?
    if unknown_letters == 0:
        guessed_word_correctly = True
        break

# muestra mensajes
if guessed_word_correctly:
    print(f'¡Ganaste! la palabra secreta es: {secret_word}')
else:
    print(f'Perdiste, la palabra secreta es: {secret_word}')
