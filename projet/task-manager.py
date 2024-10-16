# Usage : dans la console `python ./projet/task_manager.py`
print("Bienvenue dans le système de gestion des tâches DevOps !")
import os # j'importe le module (natif) `os` pour « parler » à mon système d'exploitation

tasks = []

def add_task():
    description = ""
    priority = ""

    # TANT QUE description est vide
    while not description:
        # `strip` supprime les espaces en début et din de chaîne
        description = input("Entrez la description de la tâche : ").strip()

    # TANT QUE priority est vide
    while not priority:
        priority = input("Entrez la priorité de la tâche ([H]aute, [M]oyenne, [B]asse) : ").lower()

         # SI priority est ni H ni M ni B
        if priority != "h" and priority != "m" and priority != "b":
            # ALORS erreur → j'efface la saisie utilisateur et je retourne dans ma boucle
            print("Priorité non reconnue, réponse attendue : H, M ou B")
            priority = ""


    # je crée une nouvelle tâche → dictionnaire (possible avec tuple ou list)
    task = { "description": description, "priority": priority }
    # ajoute à ma liste des tâche
    tasks.append(task)

    print("La tâche a été ajoutée avec succès !")

def main():
    # Nettoyer le terminal
    # appelle `cls` si le nom de l'OS est `nt` (Windows ?) sinon appelle `clear`
    #
    # correspond à
    # if os.name == "nt":
    #     os.system("cls")
    # else:
    #     os.system("clear")
    os.system("cls" if os.name == "nt" else "clear")
    
    print("Bienvenue dans le système de gestion des tâches DevOps !")

    while True:
        print()

        action = input("Voulez-vous [V]oir, [A]jouter, [M]odifier, [S]upprimer, [E]nregistrer ou [Q]uitter ? ")

        match action.lower():
            case "v":
                print("appeler Voir")
            case "a":
                add_task()
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