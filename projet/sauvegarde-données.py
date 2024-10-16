import json
import os

# Définir le chemin du fichier JSON
FILE_PATH = 'tasks.json'

# Fonction pour charger les tâches à partir du fichier JSON
def load_tasks():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

# Fonction pour sauvegarder les tâches dans le fichier JSON
def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

# Fonction pour ajouter une nouvelle tâche
def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)

# Fonction pour afficher les tâches
def display_tasks(tasks):
    for index, task in enumerate(tasks):
        print(f"{index + 1}: {task}")

# Programme principal
def main():
    tasks = load_tasks()
    
    while True:
        print("\nMenu:")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Quitter")
        choice = input("Choisissez une option: ")

        if choice == '1':
            task = input("Entrez la tâche à ajouter: ")
            add_task(tasks, task)
        elif choice == '2':
            print("Liste des tâches:")
            display_tasks(tasks)
        elif choice == '3':
            break
        else:
            print("Option invalide. Essayez encore.")

if __name__ == "__main__":
    main()
