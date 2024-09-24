import requests
from bs4 import BeautifulSoup

champions = [
    "Aatrox",
    "Ahri",
    "Akali",
    "Akshan",
    "Alistar",
    "Amumu",
    "Anivia",
    "Annie",
    "Aphelios",
    "Ashe",
    "Aurelion Sol",
    "Aurora",
    "Azir",
    "Bard",
    "Bel'Veth",
    "Blitzcrank",
    "Brand",
    "Braum",
    "Briar",
    "Caitlyn",
    "Camille",
    "Cassiopeia",
    "Cho'Gath",
    "Corki",
    "Darius",
    "Diana",
    "Dr. Mundo",
    "Draven",
    "Ekko",
    "Elise",
    "Evelynn",
    "Ezreal",
    "Fiddlesticks",
    "Fiora",
    "Fizz",
    "Galio",
    "Gangplank",
    "Garen",
    "Gnar",
    "Gragas",
    "Graves",
    "Gwen",
    "Hecarim",
    "Heimerdinger",
    "Hwei",
    "Illaoi",
    "Irelia",
    "Ivern",
    "Janna",
    "Jarvan IV",
    "Jax",
    "Jayce",
    "Jhin",
    "Jinx",
    "K'Sante",
    "Kai'Sa",
    "Kalista",
    "Karma",
    "Karthus",
    "Kassadin",
    "Katarina",
    "Kayle",
    "Kayn",
    "Kennen",
    "Kha'Zix",
    "Kindred",
    "Kled",
    "Kog'Maw",
    "LeBlanc",
    "Lee Sin",
    "Leona",
    "Lillia",
    "Lissandra",
    "Lucian",
    "Lulu",
    "Lux",
    "Malphite",
    "Malzahar",
    "Maokai",
    "Master Yi",
    "Milio",
    "Miss Fortune",
    "Mordekaiser",
    "Morgana",
    "Naafiri",
    "Nami",
    "Nasus",
    "Nautilus",
    "Neeko",
    "Nidalee",
    "Nilah",
    "Nocturne",
    "Nunu & Willump",
    "Olaf",
    "Orianna",
    "Ornn",
    "Pantheon",
    "Poppy",
    "Pyke",
    "Qiyana",
    "Quinn",
    "Rakan",
    "Rammus",
    "Rek'Sai",
    "Rell",
    "Renata Glasc",
    "Renekton",
    "Rengar",
    "Riven",
    "Rumble",
    "Ryze",
    "Samira",
    "Sejuani",
    "Senna",
    "Seraphine",
    "Sett",
    "Shaco",
    "Shen",
    "Shyvana",
    "Singed",
    "Sion",
    "Sivir",
    "Skarner",
    "Sona",
    "Soraka",
    "Swain",
    "Sylas",
    "Syndra",
    "Tahm Kench",
    "Taliyah",
    "Talon",
    "Taric",
    "Teemo",
    "Thresh",
    "Tristana",
    "Trundle",
    "Tryndamere",
    "Twisted Fate",
    "Twitch",
    "Udyr",
    "Urgot",
    "Varus",
    "Vayne",
    "Veigar",
    "Vel'Koz",
    "Vex",
    "Viego",
    "Viktor",
    "Vladimir",
    "Volibear",
    "Warwick",
    "Wukong",
    "Xayah",
    "Xerath",
    "Xin Zhao",
    "Yasuo",
    "Yone",
    "Yuumi",
    "Zac",
    "Zed",
    "Zeri",
    "Ziggs",
    "Zilean",
    "Zyra"
]

def get_quotes(champion_name):
    # URL de la page audio du champion
    url = f"https://leagueoflegends.fandom.com/wiki/{champion_name}/LoL/Audio"
    
    # Effectuer une requête GET à l'URL
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Erreur lors de la récupération des données pour {champion_name}: {response.status_code}")
        return []

    # Analyser le contenu de la page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Trouver tous les éléments <i> et <li> contenant des citations
    quotes = []
    
    # Récupérer les citations dans les balises <i>
    for i_tag in soup.find_all('i'):
        quote = i_tag.get_text(strip=True)
        if quote and not is_invalid_quote(quote):  # Vérifier que la citation n'est pas vide et n'est pas invalide
            quotes.append(f"{champion_name}: {quote}")
    
    # Récupérer les citations dans les balises <li>
    for li_tag in soup.find_all('li'):
        quote = li_tag.get_text(strip=True)
        if quote and not is_invalid_quote(quote):  # Vérifier que la citation n'est pas vide et n'est pas invalide
            quotes.append(f"{champion_name}: {quote}")
    
    # Filtrer et retourner les 10 premières citations uniques
    return list(dict.fromkeys(quotes))[:10]  # Supprime les doublons et limite à 10

def is_invalid_quote(quote):
    # Fonction pour déterminer si une citation est invalide
    invalid_phrases = [
        "Sound Effect",
        "15 seconds cooldown",
        "Cooldown",
        "Sound Effects",
        "plays",
        "synthwave",
        "remix",
        "to protect our land",
        "to save it",
        "waiting",
        "for Demacia",
        "together",
    ]
    
    # Vérifier si la citation contient une phrase invalide
    return any(invalid_phrase.lower() in quote.lower() for invalid_phrase in invalid_phrases)

def save_quotes_to_file(all_quotes):
    # Enregistrer toutes les citations dans un seul fichier
    with open('champion_quotes.txt', 'w', encoding='utf-8') as file:
        for quote in all_quotes:
            file.write(quote + '\n')

def main():

    
    all_quotes = []  # Liste pour stocker toutes les citations
    
    for champion in champions:
        print(f"Récupération des citations pour {champion}...")
        quotes = get_quotes(champion)
        if quotes:
            all_quotes.extend(quotes)  # Ajouter les citations à la liste globale
            print(f"{len(quotes)} citations récupérées pour {champion}.")
        else:
            print(f"Aucune citation trouvée pour {champion}.")

    # Enregistrer toutes les citations dans un seul fichier
    save_quotes_to_file(all_quotes)
    print(f"Toutes les citations ont été enregistrées dans champion_quotes.txt")

if __name__ == '__main__':
    main()
