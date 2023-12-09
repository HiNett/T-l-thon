mot_de_passe = "Tom22ble"
tips = [
    "Le mot de passe contient les trois premières lettres du prénom",
    "Le mot de passe contient l'âge de Tom",
    "Le mot de passe contient la couleur préférée de Tom"
]
compteur_tips = 0
while True:
    mot_de_passe_input = input("Entrez le mot de passe de Tom : ")
    if(mot_de_passe_input == mot_de_passe):
        print("Bravo ! Vous avez aidé Tom a retrouver son mot de passe.")
        break
    else:
        print("Mot de passe incorrect. Indice :", tips[compteur_tips % len(tips)])
        compteur_tips += 1