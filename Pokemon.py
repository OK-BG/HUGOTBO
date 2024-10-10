# ------- Classes code ------
import random
VERIF = ["oui", "non"]

# ------- Introduction ------
while True:
    pseudo = input("Veuillez choisir un pseudo : ") 
    i = input(f"Confirmez-vous vous appeler {pseudo} (oui/non) ? ")
    while i not in VERIF:
        continue
    if i == "non":
        continue
    else:
        break

print("-" * 50)
print(f"""Bienvenue dans Pokemon {pseudo}! 
Pour commencer votre aventure, choisissez un Pokemon starter !
      .
      .
      .
Vous rentrez dans la piece, 3 pokemons sont disponibles""")
print("-" * 50)
      
print("Voici les differents choix : ")
print("" * 50)
# ------- Définition ------
class Pokemon:
    def __init__(self,nombre, nom, type, PV, attaque_1, nb_attaque1, attaque_2, nb_attaque2, attaque_3, nb_attaque3, pt_attaque, counter, advantage):
        self.nombre = nombre
        self.nom = nom
        self.type = type
        self.PV = PV
        self.attaque_1 = attaque_1
        self.nb_attaque1 = nb_attaque1
        self.nb_attaque2 = nb_attaque2
        self.nb_attaque3 = nb_attaque3
        self.attaque_2 = attaque_2
        self.attaque_3 = attaque_3
        self.pt_attaque = pt_attaque
        self.counter = counter
        self.advantage = advantage
        print(f"{self.nombre} {self.nom}")

    def detail_pokemon(self):
        print("" * 50)
        print(f"""{self.nombre} {self.nom} est un Pokemon de type {self.type}. 
Ses points de vie sont de {self.PV} et son attaque de base est de {self.pt_attaque} degats.
Voici ses différentes attaques :
{self.attaque_1} (attaque de base utilisable {self.nb_attaque1} fois);
{self.attaque_2} (va avoir un effet spe. sur le pokemon utilisable {self.nb_attaque2} fois);
{self.attaque_3} (attaque spe. du pokemon utilisable {self.nb_attaque3} fois). Celle-ci inflige 1,5 fois plus de dégats;
{self.nom} resiste tres bien aux Pokemon de type {self.advantage} mais sera desaventage face a ceux de type {self.counter}. """)
        if self.attaque_2 == "Renforcement":
            print(f"""Detail effet spe. : {self.attaque_2} permet de mieux parer les coups.""")
        elif self.attaque_2 == "Concentration":
            print(f"""Detail effet spe. : {self.attaque_2} permet de taper plus fort.""")
        elif self.attaque_2 == "Esquive":
            print(f"""Detail effet spe. : {self.attaque_2} permet d'augmenter la chance d'esquiver un coup.""")

# ------- Utilisation ------        
pokemon_1 = Pokemon("(1)","Bulbizarre", "herbe", 100,"Charge", 20, "Concentration", 5, "Tranch'Herb", 2, 10, "feu", "eau")
pokemon_2 = Pokemon("(2)","Salameche", "feu", 70,"Charge", 20, "Renforcement", 5, "Flammeche", 2, 15, "eau", "herbe")
pokemon_3 = Pokemon("(3)","Carapuce", "eau", 85,"Charge", 20, "Esquive", 5, "Jet d'O", 2, 12.5, "herbe", "feu")
all_pokemon =[pokemon_1, pokemon_2, pokemon_3]

# ------- Detail Pokémon ------
print("" * 50)
CHOICE = ""
# Choix valable
while True:
    while CHOICE not in VERIF:
        CHOICE = input ("Souhaitez vous connaître les caractéristiques des Pokemons (oui/non) ? ")
    if CHOICE == "oui":
        while CHOICE not in ("1", "2", "3", "4"):
            CHOICE = input("Pour quel Pokemon souhaitez-vous les connaitres ? (1), (2), (3) (Si tous, mettez 4) : ")
# Détail du choix
            if CHOICE == "1":
                pokemon_1.detail_pokemon()  
            elif CHOICE == "2":
                pokemon_2.detail_pokemon()
            elif CHOICE == "3":
                pokemon_3.detail_pokemon()
            elif CHOICE == "4":
                for i in all_pokemon:
                    i.detail_pokemon()
                break            
    else:
        break

# ------- Sélection ------
print("" * 50)
# Choix valable
while True:
    user_1 = "" 
    while user_1 not in (pokemon_1.nom, pokemon_2.nom, pokemon_3.nom, "1", "2", "3", "4"):
        user_1 = input("Veuillez choisir un Pokemon (4 = rappel des choix) : ").capitalize()
# Choix valeur -> pokemon
    if user_1 == "1":
        user_1 = pokemon_1.nom
    elif user_1 == "2":
        user_1 = pokemon_2.nom
    elif user_1 == "3":
        user_1 = pokemon_3.nom
    elif user_1 == "4":
        print(pokemon_1.nombre,pokemon_1.nom,",", pokemon_2.nombre,pokemon_2.nom,",", pokemon_3.nombre, pokemon_3.nom)
        continue
# Confirmation du choix
    confirmation = ""
    while confirmation not in VERIF:
        confirmation = input(f"Vous voulez prendre {user_1} (oui/non) ? ")
        if confirmation == "oui":
            print(f"Vous avez choisi {user_1} !")
        elif confirmation == "non":
            break
    if confirmation == "non":
        continue
    else:
        break

if user_1 == pokemon_1.nom:
    user_1 = pokemon_1
elif user_1 == pokemon_2.nom:
    user_1 = pokemon_2
else :
    user_1 = pokemon_3
# ------- Choix adversaire ------

print(f"Pas de temps à perdre {pseudo}, {user_1.nom} veut se battre !")
print (" " * 50)

if user_1 in all_pokemon:
    all_pokemon.remove(user_1)
    adversaire_random = random.choice(all_pokemon)
    print(f"Voici votre adversaire : {adversaire_random.nom}.")
    if adversaire_random.type == user_1.counter:
        print(f"Malheureusement, {adversaire_random.nom} est de type {adversaire_random.type} ce qui lui donne l'avantage sur vous, il va faloir etre malin !")
    elif adversaire_random.type == user_1.advantage:
        print(f"Si tu perds t'es une merde.")

# ------- Combat ------
print (" " * 50)
print("Debut du combat !")
print (" " * 50)

ATTAQUE_1 = user_1.nb_attaque1 # Nombre d'attaques user
ATTAQUE_2 = user_1.nb_attaque2
ATTAQUE_3 = user_1.nb_attaque3

B_ATTAQUE_1 = adversaire_random.nb_attaque1 # Nombre d'attaques bot
B_ATTAQUE_2 = adversaire_random.nb_attaque2
B_ATTAQUE_3 = adversaire_random.nb_attaque3

ATTAQUE_SPE = user_1.pt_attaque # Attaques après effets
B_ATTAQUE_SPE = adversaire_random.pt_attaque

SKIP_ATTAQUE = False
B_SKIP_ATTAQUE = False

while user_1.PV and adversaire_random.PV > 0:
    i = "" # Choix attaque user et bot
    j = random.choice([adversaire_random.attaque_1, adversaire_random.attaque_2, adversaire_random.attaque_3])
# Choix attaque
    while i not in (user_1.attaque_1, user_1.attaque_2, user_1.attaque_3, "1", "2", "3", "4"):
        i = input(f"""Que souhaitez vous faire ?
(1 = attaque de base,
 2 = effet spe.,
 3 = attaque spe.,
 4 = rappel des attaques) : """)
        print (" " * 50)

        if i == "4":
            print(f"""Voici vos attaques possibles :
{user_1.attaque_1} ({ATTAQUE_1} / {user_1.nb_attaque1});
{user_1.attaque_2} ({ATTAQUE_2} / {user_1.nb_attaque2});
{user_1.attaque_3} ({ATTAQUE_3} / {user_1.nb_attaque3})""")
            print("" * 50)
            continue
# Esquive bot
        w = z = "Esquive"

        if z in adversaire_random.attaque_2:
            tirages_bot = 6 - B_ATTAQUE_2
            for b in range(tirages_bot):
                flop_bot = random.randint(1, 10)
                echec_bot = random.randint(1, 10)
                if flop_bot == echec_bot:
                    B_SKIP_ATTAQUE = True
        
        if B_SKIP_ATTAQUE and i not in ("2", user_1.attaque_2) :
            user_1.pt_attaque = 0
            print(f"{user_1.nom} a utilise {i}")
            print(f"{adversaire_random.nom} fait un isch-isch")
            print(f"Quel isch-isch! L'attaque de {user_1.nom} echoue.")
            B_SKIP_ATTAQUE = False
# Attaques user
        
        else :
            if i in (user_1.attaque_1, "1") and ATTAQUE_1 > 0: # Attaque 1
                ATTAQUE_1 -= 1
                print(f"Vous avez utilise {user_1.attaque_1}.")
                adversaire_random.PV -= ATTAQUE_SPE
                print(f"{user_1.nom} a mis une mandale de {int(ATTAQUE_SPE)} degats.")
            elif i in (user_1.attaque_1, "1") and ATTAQUE_1 == 0:
                print(f"Vous ne pouvez plus utiliser {user_1.attaque_1}...")
                continue
        
            if i in (user_1.attaque_2, "2") and ATTAQUE_2 > 0: # Attaque 2
                print(f"Vous avez utilise {user_1.attaque_2}.")

                if i == "Renforcement":
                    B_ATTAQUE_SPE /= 1.25
                    print(f"{user_1.nom} est pret a prendre des grosses mandales.")
                elif i == "Concentration":
                    print(f"{user_1.nom} est pret a mettre des grosses mandales.")
                    ATTAQUE_SPE *= 1.25    
                ATTAQUE_2 -= 1
            elif i in (user_1.attaque_2, "2") and ATTAQUE_2 == 0:
                print(f"Vous ne pouvez plus utiliser {user_1.attaque_2}...")
                continue

            if i in (user_1.attaque_3, "3") and ATTAQUE_3 > 0: # Attaque 3
                ATTAQUE_3 -= 1
                print(f"Vous avez utilise {user_1.attaque_3}.")
                if user_1.type == adversaire_random.counter:
                    adversaire_random.PV -= ATTAQUE_SPE * 1.5
                    print(f"{user_1.nom} a deglinguer le gros crane de {adversaire_random.nom} avec {int(ATTAQUE_SPE * 1.5)} degats.")
                else :
                    adversaire_random.PV -= ATTAQUE_SPE / 1.5
                    print(f"{user_1.nom} a mis une caresse de {int(ATTAQUE_SPE / 1.5)} degats.")
            elif i in (user_1.attaque_3, "3") and ATTAQUE_3 == 0:
                print(f"Vous ne pouvez plus utiliser {user_1.attaque_3}...")
                continue
# Victoire user       
        if adversaire_random.PV <= 0:
            print(f"{adversaire_random.nom} est decede... quel crack vous avez gagnez du riz")
            print (" " * 50)
            print("Vous avez maintenant du riz.")
            break 
# Esquive user
        if w in user_1.attaque_2:
            tirages = 6 - ATTAQUE_2
            for a in range(tirages):
                flop = random.randint(1, 10)
                echec = random.randint(1, 10)
                if flop == echec:
                    SKIP_ATTAQUE = True
        if SKIP_ATTAQUE and j not in (adversaire_random.attaque_2):
            adversaire_random.pt_attaque = 0
            print(f"{adversaire_random.nom} a utilise {j}")
            print(f"{user_1.nom} fait un isch-isch")
            print(f"Quel isch-isch! L'attaque de {adversaire_random.nom} echoue.")
            SKIP_ATTAQUE = False                                
# Attaques bot
    
        
        else :
            if j == adversaire_random.attaque_1 and B_ATTAQUE_1 > 0: # Attaque 1
                B_ATTAQUE_1 -= 1
                print(f"{adversaire_random.nom} a utilise {adversaire_random.attaque_1}.")
                user_1.PV -= B_ATTAQUE_SPE
                print(f"{adversaire_random.nom} a mis une mandale de {int(B_ATTAQUE_SPE)} degats.")
    
            if j == adversaire_random.attaque_2 and B_ATTAQUE_2 > 0: # Attaque 2
                print(f"{adversaire_random.nom} a utilise {adversaire_random.attaque_2}.")
                if j == "Renforcement":
                    ATTAQUE_SPE /= 1.25
                    print(f"Les claques de {user_1.nom} vont etre de plus en plus timides.")
                elif j == "Concentration":
                    print(f"{user_1.nom}, prepare tes fesses.")
                    B_ATTAQUE_SPE *= 1.25     
                B_ATTAQUE_2 -= 1
    
            if j == adversaire_random.attaque_3 and B_ATTAQUE_3 > 0: # Attaque 3
                print(f"{adversaire_random.nom} a utilise {adversaire_random.attaque_3}.")
                B_ATTAQUE_3 -= 1
                if adversaire_random.type == user_1.counter: 
                    user_1.PV -= B_ATTAQUE_SPE * 1.5
                    print(f"{adversaire_random.nom} a deglinguer le gros crane de {user_1.nom} avec {int(B_ATTAQUE_SPE * 1.5)} degats.")
                else :
                    user_1.PV -= B_ATTAQUE_SPE / 1.5
                    print(f"{adversaire_random.nom} a mis une caresse de {int(B_ATTAQUE_SPE / 1.5)} degats.")

    if user_1.PV <= 0:
        print(f"{user_1.nom} est decede... vous avez perdu retour dodo")
    elif ATTAQUE_1 and ATTAQUE_2 and ATTAQUE_3 == 0:
        print("T'es au bout du jus mon gars rentre chez toi.")
        break
# Resume du tour
    else:
        print(f"{user_1.nom} a {int(user_1.PV)} PV contre {int(adversaire_random.PV)} pour {adversaire_random.nom}.")
        print("Prochain tour ! ")
        print (" " * 50)
    

        
    
    
    



            
                

