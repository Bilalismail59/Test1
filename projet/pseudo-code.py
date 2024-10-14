# INITIALISER une liste vide pour les tâches
taches = []

# FONCTION ajouter_tâche()
def ajouter_tache():
    description = input("Entrez la description de la tâche : ")
    priorite = input("Entrez la priorité de la tâche (haute, moyenne, basse) : ").lower()
    
    if priorite not in ["haute", "moyenne", "basse"]:
        print("Priorité non valide. La tâche ne sera pas ajoutée.")
        return
    
    tache = {"description": description, "priorité": priorite}
    taches.append(tache)
    print("Tâche ajoutée avec succès !")

# FIN FONCTION

# FONCTION afficher_tâches()
def afficher_taches():
    if not taches:
        print("Aucune tâche à afficher.")
    else:
        print("\nListe des tâches :")
        for i, tache in enumerate(taches, start=1):
            print(f"{i}. {tache['description']} (Priorité : {tache['priorité']})")
# FIN FONCTION

# FONCTION modifier_tâche()
def modifier_tache():
    afficher_taches()
    
    if taches:
        numero = int(input("Entrez le numéro de la tâche à modifier : "))
        
        if 1 <= numero <= len(taches):
            tache = taches[numero - 1]
            nouvelle_description = input(f"Entrez la nouvelle description (actuelle : {tache['description']}) : ")
            nouvelle_priorite = input(f"Entrez la nouvelle priorité (actuelle : {tache['priorité']}) : ").lower()
            
            if nouvelle_priorite not in ["haute", "moyenne", "basse"]:
                print("Priorité non valide. La tâche ne sera pas modifiée.")
            else:
                tache['description'] = nouvelle_description or tache['description']
                tache['priorité'] = nouvelle_priorite or tache['priorité']
                print("Tâche modifiée avec succès !")
        else:
            print("Numéro de tâche invalide.")
# FIN FONCTION

# FONCTION supprimer_tâche()
def supprimer_tache():
    afficher_taches()
    
    if taches:
        numero = int(input("Entrez le numéro de la tâche à supprimer : "))
        
        if 1 <= numero <= len(taches):
            taches.pop(numero - 1)
            print("Tâche supprimée avec succès !")
        else:
            print("Numéro de tâche invalide.")
# FIN FONCTION

# FONCTION principale()
def principale():
    print("Bienvenue dans le système de gestion des tâches DevOps !")
    
    while True:
        action = input("\nQue souhaitez-vous faire ? (ajouter, afficher, modifier, supprimer, quitter) : ").lower()
        
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
            print("Action non reconnue.")
# FIN FONCTION

# APPELER principale()
principale()
