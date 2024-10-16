# Usage : dans la console `python ./projet/task_manager.py`
print("Bienvenue dans le système de gestion des tâches DevOps !")
import os # j'importe le module (natif) `os` pour « parler » à mon système d'exploitation

tasks = []
priority_levels = {
    "h": "Haute",
    "m": "Moyenne",
    "b": "Basse",
    "t": "Top",
}

def get_priority_options():
    """
    Retourne `[H]aute, [M]oyenne, [B]asse` depuis le dictionnaire des priorités
    """
    result = []

    # `dictionnaire.values()` crée une liste avec toutes les valeurs du dictionnaire
    # → ['Haute', 'Moyenne', 'Basse']
    # POUR CHAQUE valeur de mon dictionnaire
    for priority in priority_levels.values():
        result.append(f"[{priority[0].upper()}]{priority[1:]}")

    # → ['[H]aute', '[M]oyenne', '[B]asse']

    # concatène les éléments de ma liste en les séparant par `, `
    # → [H]aute, [M]oyenne, [B]asse
    return ', '.join(result)


def get_priority_initials():
    """
    Retourne `H, M, B` depuis le dictionnaire des priorités
    """
    # `dictionnaire.keys()` crée une liste avec toutes les clés du dictionnaire
    # → ['h', 'm', 'b']
    # concatène les éléments de ma liste en les séparant par `, `
    # → h, m, b
    return ', '.join(priority_levels.keys()).upper()


def add_task():
    description = ""
    priority = ""

    # TANT QUE description est vide
    while not description:
        # `strip` supprime les espaces en début et din de chaîne
        description = input("Entrez la description de la tâche : ").strip()

    # TANT QUE priority est vide
    while not priority:
        priority = input(f"Entrez la priorité de la tâche ({get_priority_options()}) : ").strip().lower()

        # SI priority n'est pas une initiale de mon dictionnaire de niveaux de propriétés
        # `priority_levels.keys()` → ['h', 'm', 'b', 't']
        if not priority in priority_levels.keys():
            # ALORS erreur → j'efface la saisie utilisateur et je retourne dans ma boucle
            print(f"Priorité non reconnue, réponse attendue : {get_priority_initials()}")
            priority = ""

    # je crée une nouvelle tâche → dictionnaire (possible avec tuple ou list)
    # je vais chercher l'élément de mon dictionnaire qui a pour clé la valeur stockée dans `priority` (h, m ou b)
    priority_label = priority_levels[priority]
    task = { "description": description, "priority": priority_label }
    # ajoute à ma liste des tâche
    tasks.append(task)

    print("La tâche a été ajoutée avec succès !")


def display_tasks():
    if not tasks:
        print("Aucune tâche à afficher")
        return # arrête l'exécution de la fonction (on sort de la fonction)
    
    # for task in tasks:
    #     # print(task) # → {'description': 'nom tâche', 'priority': 'Haute'}
    #     print(f"\t{task['description']} – [{task['priority']}]")

    print("Liste des tâches actuelles :")

    # `enumerate()` permet de récupérer la tâche et son index dans la liste des tâches
    for task_index, task in enumerate(tasks, start=1):
        print(f"\t[{task_index}] {task['description']} (Priorité : {task['priority']})")


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
                display_tasks()
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