import unittest

import os
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        
        """Configurer le test avec un fichier temporaire."""
        self.manager = TaskManager('test_tasks.json')
        self.manager.clear_tasks()  # Assurer un état propre

    def test_add_task(self):
        self.manager.add_task('Test Task 1')
        self.assertIn('Test Task 1', self.manager.display_tasks())

    def test_remove_task(self):
        self.manager.add_task('Task to Remove')
        self.manager.remove_task(0)  # Supprime la première tâche
        self.assertNotIn('Task to Remove', self.manager.display_tasks())

    def test_load_tasks(self):
        self.manager.add_task('Persistent Task')
        self.manager.save_tasks()  # Sauvegarder les tâches
        new_manager = TaskManager('test_tasks.json')
        self.assertIn('Persistent Task', new_manager.display_tasks())

    def tearDown(self):
        """Supprimer le fichier temporaire après les tests."""
        if os.path.exists('test_tasks.json'):
            os.remove('test_tasks.json')

if __name__ == '__main__':
    unittest.main()
