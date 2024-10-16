# Pseudo code du projet fil rouge

```text
DEBUT

INITIALISER une liste vide pour les tâches

FONCTION ajouter_tâche()
    DEMANDER à l'utilisateur d'entrer la description de la tâche
    DEMANDER à l'utilisateur d'entrer la priorité de la tâche (haute, moyenne, basse)
    
    CRÉER une variable/dictionnaire pour la tâche avec sa description et sa priorité
    AJOUTER la tâche à la liste des tâches
    AFFICHER "La tâche a été ajoutée avec succès !"
FIN FONCTION

FONCTION afficher_tâches()
    SI la liste des tâches est vide ALORS 
        AFFICHER "Aucune à afficher"
    SINON
        AFFICHER "Les tâches :"

        POUR CHAQUE tâche DANS la liste des tâches FAIRE
            AFFICHER la description et la priorité de la tâche (+ discriminant → identifiant)
        FIN POUR
    FIN SI
FIN FONCTION

FONCTION modifier_tâche()
    APPELER afficher_tâches()

    DEMANDER à l'utilisateur d'entrer le discriminant de la tâche à modifier

    SI le discriminant est valide ALORS
        DEMANDER à l'utilisateur d'entrer la nouvelle description
        DEMANDER à l'utilisateur d'entrer la nouvelle priorité
        METTRE À JOUR la tâche dans la liste
        AFFICHER "La tâche a été modifiée avec succès !"
    SINON
        AFFICHER "Le discriminant n'est pas valide"
    FIN SI
FIN FONCTION

FONCTION supprimer_tâche()
    APPELER afficher_tâches()

    DEMANDER à l'utilisateur d'entrer le discriminant de la tâche à supprimer

    SI le discriminant est valide ALORS
        SUPPRIMER la tâche dans la liste
        AFFICHER "La tâche a été supprimée avec succès !"
    SINON
        AFFICHER "Le discriminant n'est pas valide"
    FIN SI
FIN FONCTION

FONCTION principale()
    AFFICHER "Bienvenue dans le système de gestion des tâches DevOps !"
    TANT QUE VRAI FAIRE
        DEMANDER à l'utilisateur quelle action il souhaite effectuer (ajouter, afficher, modifier, supprimer ou quitter)
        SI action est "ajouter" ALORS
            APPELER ajouter_tâche()
        SINON SI action est "afficher" ALORS
            APPELER afficher_tâches()
        SINON SI action est "modifier" ALORS
            APPELER modifier_tâche()
        SINON SI action est "supprimer" ALORS
            APPELER supprimer_tâche()
        SINON SI action est "quitter" ALORS
            SORTIR de la boucle
        SINON
            AFFICHER "Action non reconnue."
        FIN SI
    FIN TANT QUE
FIN FONCTION

APPELER principale()

FIN
```