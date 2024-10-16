class Tache:
    def __init__(self, description, priorite):
        self.description = description
        self.priorite = priorite
        self.id = id(self)  # Utilisation de l'identifiant unique de l'objet

class GestionTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self):
        description = input("Entrez la description de la tâche : ")
        priorite = input("Entrez la priorité de la tâche (haute, moyenne, basse) : ")
        nouvelle_tache = Tache(description, priorite)
        self.taches.append(nouvelle_tache)
        print("La tâche a été ajoutée avec succès !")

    def afficher_taches(self):
        if not self.taches:
            print("Aucune tâche à afficher.")
        else:
            print("Les tâches :")
            for tache in self.taches:
                print(f"ID: {tache.id}, Description: {tache.description}, Priorité: {tache.priorite}")

    def modifier_tache(self):
        self.afficher_taches()
        try:
            discriminant = int(input("Entrez l'ID de la tâche à modifier : "))
            tache_a_modifier = next(tache for tache in self.taches if tache.id == discriminant)
            tache_a_modifier.description = input("Entrez la nouvelle description : ")
            tache_a_modifier.priorite = input("Entrez la nouvelle priorité : ")
            print("La tâche a été modifiée avec succès !")
        except StopIteration:
            print("Le discriminant n'est pas valide.")
        except ValueError:
            print("Entrée invalide.")

    def supprimer_tache(self):
        self.afficher_taches()
        try:
            discriminant = int(input("Entrez l'ID de la tâche à supprimer : "))
            self.taches = [tache for tache in self.taches if tache.id != discriminant]
            print("La tâche a été supprimée avec succès !")
        except ValueError:
            print("Entrée invalide.")

    def principale(self):
        print("Bienvenue dans le système de gestion des tâches DevOps !")
        while True:
            action = input("Que souhaitez-vous faire ? (ajouter, afficher, modifier, supprimer, quitter) : ")
            if action == "ajouter":
                self.ajouter_tache()
            elif action == "afficher":
                self.afficher_taches()
            elif action == "modifier":
                self.modifier_tache()
            elif action == "supprimer":
                self.supprimer_tache()
            elif action == "quitter":
                break
            else:
                print("Action non reconnue.")

if __name__ == "__main__":
    gestionnaire = GestionTaches()
    gestionnaire.principale()
