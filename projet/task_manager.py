import json
import os

class TaskManager:
    def __init__(self, file_path='tasks.json'):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Charge les tâches à partir d'un fichier JSON."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        """Sauvegarde les tâches dans le fichier JSON."""
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        """Ajoute une nouvelle tâche."""
        self.tasks.append(task)
        self.save_tasks()

    def display_tasks(self):
        """Affiche toutes les tâches."""
        return self.tasks

    def remove_task(self, index):
        """Supprime une tâche par son index."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def clear_tasks(self):
        """Efface toutes les tâches."""
        self.tasks.clear()
        self.save_tasks()
