
"""Test saving and reloading users, projects, and tasks."""

import tempfile
from pathlib import Path

from manager import ProjectManager


def main():
    """Check that application records survive a reload."""

    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "database.json"

        # Create a manager that uses a temporary database.
        manager = ProjectManager(file_path)

        # Create three users.
        hanifa = manager.add_user(
            "Hanifa", "hanifah52@gmail.com"
        )
        jeff = manager.add_user(
            "Jeff", "jeff@gmail.com"
        )
        zackary = manager.add_user(
            "Zackary", "zackary33@gmail.com"
        )

        # Create a project and assign it to Hanifa.
        project = manager.add_project(
            "Clothing Collection Design",
            "Design the first clothing collection",
            "2026-12-31",
            hanifa.id,
        )

        # Create a task with two contributors.
        task = manager.add_task(
            "Finalize garment sketches",
            project.id,
            contributor_ids=[hanifa.id, jeff.id],
        )

        print("Users, project, and task created.")

        # Create a fresh manager to simulate restarting the app.
        reloaded = ProjectManager(file_path)

        print("\n=== RELOADED DATA ===")
        print("Users:", len(reloaded.users))
        print("Projects:", len(reloaded.projects))
        print("Tasks:", len(reloaded.tasks))

        restored_task = reloaded.get_task(task.id)

        print("\nRestored project:", restored_task.project.title)
        print("Restored task:", restored_task.title)
        print(
            "Restored contributors:",
            ", ".join(
                user.name for user in restored_task.contributors
            ),
        )

        # Verify the data and relationships.
        assert len(reloaded.users) == 3
        assert len(reloaded.projects) == 1
        assert len(reloaded.tasks) == 1
        assert restored_task.project.owner.name == "Hanifa"
        assert len(restored_task.contributors) == 2

        # Verify that task completion also persists.
        reloaded.complete_task(task.id)
        checked_again = ProjectManager(file_path)

        assert checked_again.get_task(task.id).status == "Complete"

        print("\nTask completion persisted.")
        print("All persistence checks passed!")


if __name__ == "__main__":
    main()
