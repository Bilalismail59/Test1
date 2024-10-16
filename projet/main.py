from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nMenu:")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        choice = input("Choisissez une option: ")

        if choice == '1':
            task = input("Entrez la tâche à ajouter: ")
            manager.add_task(task)
        elif choice == '2':
            tasks = manager.display_tasks()
            print("Liste des tâches:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}: {task}")
        elif choice == '3':
            index = int(input("Entrez le numéro de la tâche à supprimer: ")) - 1
            manager.remove_task(index)
        elif choice == '4':
            break
        else:
            print("Option invalide. Essayez encore.")

if __name__ == "__main__":
    main()

    



# # C'est une autre partie de code
# nombres = {1, 2, 3, 4, 5}

# nombres.add(6)
# nombres.add(6)
# print(nombres)

# numbres = [1,2,3,4,5,6, 6, 5, 4, 3, 2, 1]
# unique_numbres = set(numbres)
# print(unique_numbres)

# age_str = "25"  # Exemple d'entrée, assurez-vous que c'est bien une chaîne représentant un nombre
# age_int = float(age_str)  # Conversion de la chaîne en nombre flottant
# print(age_int)



