# Cahier des Charges : Système de Gestion des Tâches DevOps

## 1. Contexte

Dans un environnement DevOps, la gestion efficace des tâches est cruciale pour garantir la fluidité des opérations et le respect des délais. Ce projet vise à développer un système qui permet aux équipes de suivre, prioriser et gérer leurs tâches de manière collaborative.

## 2. Objectifs

- **Outil de Gestion des Tâches** : Créer un outil qui facilite le suivi des activités au sein d'une équipe DevOps.
- **Priorisation des Tâches** : Permettre aux utilisateurs de classer les tâches par priorité (haute, moyenne, basse).
- **Persistance des Données** : Assurer la sauvegarde et le chargement des tâches à partir d'un fichier JSON, permettant ainsi la persistance des données entre les sessions.

## 3. Fonctionnalités Principales

- **Choix de l'opération** : Les utilisateurs doivent pouvoir choisir entre différentes actions : ajouter, afficher, modifier, supprimer, enregistrer ou quitter.
- **Ajout de Tâches** : Les utilisateurs doivent pouvoir ajouter des tâches avec une description et une priorité.
- **Affichage des Tâches** : Les utilisateurs doivent pouvoir afficher toutes les tâches existantes avec leurs détails.
- **Modification de Tâches** : Permettre aux utilisateurs de modifier la description et la priorité d'une tâche existante.
- **Suppression de Tâches** : Les utilisateurs doivent pouvoir supprimer des tâches de la liste.
- **Sauvegarde et Chargement** : Implémenter des fonctionnalités pour sauvegarder les tâches dans un fichier JSON et charger ces tâches au démarrage de l'application.

## 4. Contraintes Techniques

- **Interface en Ligne de Commande** : L'outil doit être accessible via une interface en ligne de commande conviviale.
- **Interaction Utilisateur** : Les utilisateurs doivent pouvoir interagir avec le système sans avoir besoin de modifier le code source.
- **Stockage des Données** : Les tâches doivent être stockées dans un fichier JSON, garantissant la persistance des données entre les sessions.
- **Documentation** : Le code doit être bien commenté et structuré pour faciliter la maintenance et la compréhension par d'autres développeurs.

## 6. Livrables

- **Code Source** : Le code complet de l'application de gestion des tâches.
- **Documentation Technique** : Documentation détaillant l'architecture du code, les fonctionnalités et les instructions d'utilisation.

## 7. Échéancier

- **Durée du Projet** : 4 jours, avec des objectifs spécifiques à atteindre chaque jour.
- **Jours de Développement** :
   - **Jour 1** : Conception de l'algorithme et mise en place de la structure de base.
   - **Jour 2** : Ajout et affichage des tâches.
   - **Jour 3** : Modification et suppression de tâches.
   - **Jour 4** : Persistance des données et finalisation du projet.