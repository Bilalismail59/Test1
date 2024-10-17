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

    for priority in priority_levels.values():
        result.append(f"[{priority[0].upper()}]{priority[1:]}")

    return ', '.join(result)


def get_priority_initials():
    """
    Retourne `H, M, B` depuis le dictionnaire des priorités
    """
    return ', '.join(priority_levels.keys()).upper()


def add_task():
    description = ""
    priority = ""

    while not description:
        description = input("Entrez la description de la tâche : ").strip()

    while not priority:
        priority = input(f"Entrez la priorité de la tâche ({get_priority_options()}) : ").strip().lower()

        if not priority in priority_levels.keys():
            print(f"Priorité non reconnue, réponse attendue : {get_priority_initials()}")
            priority = ""

    priority_label = priority_levels[priority]
    task = { "description": description, "priority": priority_label }
    tasks.append(task)

    print("La tâche a été ajoutée avec succès !")


def display_tasks():
    if not tasks:
        print("Aucune tâche à afficher")
        return
    
    print("Liste des tâches actuelles :")

    for task_index, task in enumerate(tasks, start=1):
        print(f"\t[{task_index}] {task['description']} (Priorité : {task['priority']})")


def edit_task():
    # on récupère l'index saisi par l'utilisateur (+ gestion des erreurs)
    index = ask_index("modifier")

    print("Note : laissez le champ vide pour ne pas le modifier")

    # on récupère les champs saisis
    description = input('Entrez la description de la tâche : ').strip()
    priority = input(f"Entrez la priorité de la tâche ({get_priority_options()}) : ").strip().lower()

    # SI on a une description, on la modifie dans la liste des tâches
    # (SINON on laisse comme ça, on fait rien)
    if description:
        tasks[index - 1]["description"] = description

    # SI on a une priorité, on la modifie dans la liste des tâches
    # (SINON on laisse comme ça, on fait rien)
    if priority and priority in priority_levels.keys():
        tasks[index - 1]["priority"] = priority_levels[priority]

    print("La tâche a été modifiée avec succès !")


def delete_task():
    index = ask_index("supprimer")
    # on supprime l'élément de la liste à l'index `index - 1`
    tasks.pop(index - 1)

    print("La tâche a été supprimée avec succès !")


def save_tasks():
    pass


def ask_index(action):
    display_tasks()

    # TANT QUE l'index saisi n'est pas valide
    while True:
        index = input(f"Saisir l'index de la tâche à {action} : ").strip()

        # est-ce que la saisie est un chiffre et correspond à un index de ma liste
        if index.isdigit() and 1 <= int(index) <= len(tasks):
            index = int(index)
            break
        else:
            print('Veuillez saisir un index de tâche valide.')

    # on retourne l'index saisi pour utilisation dans edit et delete
    return index

def main():
    os.system("cls" if os.name == "nt" else "clear")
    
    print("Bienvenue dans le système de gestion des tâches DevOps !")

    while True:
        print()

        action = input("Voulez-vous [V]oir, [A]jouter, [M]odifier, [S]upprimer, [E]nregistrer ou [Q]uitter ? ").strip()

        match action.lower():
            case "v":
                display_tasks()
            case "a":
                add_task()
            case "m":
                edit_task()
            case "s":
                delete_task()
            case "e":
                save_tasks()
            case "q":
                print("À bientôt !")
                break
            case _:
                print("Action inconnue")
                print("Merci d'utiliser la première lettre de l'action à effectuer")


if __name__ == "__main__":
    main()



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