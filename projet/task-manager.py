# Usage : dans la console `python ./projet/task_manager.py`
import os # j'importe le module (natif) `os` pour « parler » à mon système d'exploitation

tasks = []

def main():
     # Nettoyer le terminal
    # appelle `cls` si le nom de l'OS est `nt` (Windows ?) sinon appelle `clear`
    #
    # correspond à
    # if os.name == "nt":
    #     os.system("cls")
    # else:
    #     os.system("clear")

    os.system('cls' if os.name=='nt' else 'clear')
    
    print("Bienvenue dans le système de gestion des tâches DevOps !")

    while True:
        print()

        action = input("Voulez-vous [V]oir, [A]jouter, [M]odifier, [S]upprimer, [E]nregistrer ou [Q]uitter ? ")

        match action.lower():
            case "v":
                print("appeler Voir")
            case "a":
                print("appeler Ajouter")
            case "m":
                print("appeler Modifier")
            case "s":
                print("appeler Supprimer")
            case "e":
                print("appeler Enregistrer")
            case "q":
                print("À bientôt !")
                break # permet de sortir de la boucle
            case _:
                print("Action inconnue")
                print("Merci d'utiliser la première lettre de l'action à effectuer")


if __name__ == "__main__":
    # `__name__` variable spéciale qui contient le nom du module :

    #     - vaut `__main__` si ce fichier est exécuté directement
    #     - vaut `task_manager` (nom du module) si ce fichier est importé

    # Cette condition est courante en Python pour s'assurer de n'appeler la fonction
    # principale que si le fichier est directement exécuté.
    main()