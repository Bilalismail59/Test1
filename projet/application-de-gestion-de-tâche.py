# Initialiser une liste vide pour les tâches
taches = []

# Fonction pour ajouter une tâche
def ajouter_tache():
    description = input("Entrez la description de la tâche : ")
    priorite = input("Entrez la priorité de la tâche (haute, moyenne, basse) : ")
    
    # Créer un dictionnaire pour la tâche
    tache = {
        "description": description,
        "priorite": priorite
    }
    
    # Ajouter la tâche à la liste
    taches.append(tache)
    print("La tâche a été ajoutée avec succès !")

# Fonction pour afficher toutes les tâches
def afficher_taches():
    if not taches:
        print("Aucune tâche à afficher.")
    else:
        print("Les tâches :")
        for idx, tache in enumerate(taches):
            print(f"{idx+1}. {tache['description']} (Priorité : {tache['priorite']})")

# Fonction pour modifier une tâche
def modifier_tache():
    afficher_taches()
    try:
        index = int(input("Entrez l'identifiant de la tâche à modifier : ")) - 1
        if 0 <= index < len(taches):
            description = input("Entrez la nouvelle description de la tâche : ")
            priorite = input("Entrez la nouvelle priorité de la tâche (haute, moyenne, basse) : ")
            
            # Mettre à jour la tâche
            taches[index]['description'] = description
            taches[index]['priorite'] = priorite
            print("La tâche a été modifiée avec succès !")
        else:
            print("L'identifiant n'est pas valide.")
    except ValueError:
        print("Veuillez entrer un identifiant valide.")

# Fonction pour supprimer une tâche
def supprimer_tache():
    afficher_taches()
    try:
        index = int(input("Entrez l'identifiant de la tâche à supprimer : ")) - 1
        if 0 <= index < len(taches):
            # Supprimer la tâche de la liste
            del taches[index]
            print("La tâche a été supprimée avec succès !")
        else:
            print("L'identifiant n'est pas valide.")
    except ValueError:
        print("Veuillez entrer un identifiant valide.")

# Fonction principale du programme
def principale():
    print("Bienvenue dans le système de gestion des tâches DevOps !")
    
    while True:
        print("\nOptions : ajouter, afficher, modifier, supprimer, quitter")
        action = input("Quelle action souhaitez-vous effectuer ? ").lower()
        
        if action == "ajouter":
            ajouter_tache()
        elif action == "afficher":
            afficher_taches()
        elif action == "modifier":
            modifier_tache()
        elif action == "supprimer":
            supprimer_tache()
        elif action == "quitter":
            print("Au revoir !")
            break
        else:
            print("Action non reconnue, veuillez réessayer.")

# Appel de la fonction principale pour démarrer le programme
principale()
