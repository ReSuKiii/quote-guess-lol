from get_quotes import champions
from random import *


def quiz():
    # Demander à l'utilisateur de deviner le champion à partir de la citation, ne passe pas au suivant tant que la réponse n'est pas correcte
    with open('champion_quotes.txt', 'r', encoding='utf-8') as file:
        quotes = file.readlines()
    
    total = len(quotes)
    score = 0
    print(f"Devinez le champion à partir de la citation. Vous avez {total} citations à deviner.\n")
    
    shuffle(quotes)
    for quote in quotes:
        champion, quote = quote.split(':', 1)
        guess = input(f"Quel champion a dit : {quote.strip()} ? ")

        while guess.lower() != champion.lower():
            if guess.lower() == "exit" or guess.lower() == "quitter" or guess.lower() == "e" or guess.lower() == "q":
                print("\nQuiz interrompu.")
                print(f"Votre score est de {score}.")
                return
            elif guess.lower() == "next" or guess.lower() == "suivant" or guess.lower() == "n" or guess.lower() == "s":
                break
            guess = input(f"Non, essayez encore. Quel champion a dit : {quote.strip()} ? ")
        if guess.lower() == champion.lower():
            print("Correct!\n")
            score += 1

    print(f"Quiz terminé! Votre score est de {score}.")

try:
    if __name__ == "__main__":
        quiz()
except(KeyboardInterrupt):
    print("\nQuiz interrompu.")
    
