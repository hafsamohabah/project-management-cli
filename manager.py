
"""Manage users, projects, tasks, and JSON persistence."""

from datetime import date

from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data


class ProjectManager:
    """Manage application records and their relationships."""

    def __init__(self, file_path="data/database.json"):
        """Initialize the manager and load saved records."""
        self.file_path = file_path
        self.users = []
        self.projects = []
        self.tasks = []
        self.load()

    def load(self):
        """Load saved records and rebuild their relationships."""
        data = load_data(self.file_path)

        self.users = []
        self.projects = []
        self.tasks = []

        users_by_id = {}

        for record in data["users"]:
            user = User(record["name"], record["email"])
            user._id = record["id"]
            users_by_id[user.id] = user
            self.users.append(user)

        projects_by_id = {}

        for record in data["projects"]:
            owner_id = record["owner_id"]

            if owner_id not in users_by_id:
                raise ValueError(
                    f"Project {record['id']} references "
                    f"unknown user {owner_id}."
                )

            project = Project(
                record["title"],
                record["description"],
                date.fromisoformat(record["due_date"]),
                users_by_id[owner_id],
            )
            project._id = record["id"]
            projects_by_id[project.id] = project
            self.projects.append(project)
            project.owner.add_project(project)

        for record in data["tasks"]:
            project_id = record["project_id"]

            if project_id not in projects_by_id:
                raise ValueError(
                    f"Task {record['id']} references "
                    f"unknown project {project_id}."
                )

            task = Task(record["title"], projects_by_id[project_id])
            task._id = record["id"]
            task.status = record["status"]

            for user_id in record.get("contributor_ids", []):
                if user_id not in users_by_id:
                    raise ValueError(
                        f"Task {record['id']} references "
                        f"unknown user {user_id}."
                    )
                task.add_contributor(users_by_id[user_id])

            task.project.add_task(task)
            self.tasks.append(task)

        # Keep generated IDs above the largest IDs already loaded.
        User._next_id = max(users_by_id, default=0) + 1
        Project._next_id = max(projects_by_id, default=0) + 1
        Task._next_id = max(
            (task.id for task in self.tasks),
            default=0,
        ) + 1

    def save(self):
        """Convert application objects to dictionaries and save them."""
        data = {
            "users": [
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                }
                for user in self.users
            ],
            "projects": [
                {
                    "id": project.id,
                    "title": project.title,
                    "description": project.description,
                    "due_date": project.due_date.isoformat(),
                    "owner_id": project.owner.id,
                }
                for project in self.projects
            ],
            "tasks": [
                {
                    "id": task.id,
                    "title": task.title,
                    "status": task.status,
                    "project_id": task.project.id,
                    "contributor_ids": [
                        user.id for user in task.contributors
                    ],
                }
                for task in self.tasks
            ],
        }

        save_data(data, self.file_path)

    def add_user(self, name, email):
        """Create and register a user."""
        if any(user.email.lower() == email.lower() for user in self.users):
            raise ValueError("A user with this email already exists.")

        user = User(name, email)
        self.users.append(user)
        self.save()
        return user

    def add_project(self, title, description, due_date, owner_id):
        """Create and register a project for an existing user."""
        owner = self.get_user(owner_id)

        project = Project(title, description, due_date, owner)
        owner.add_project(project)
        self.projects.append(project)
        self.save()
        return project

    def add_task(self, title, project_id, contributor_ids=None):
        """Create a task for a project and assign contributors."""
        project = self.get_project(project_id)
        contributors = [
            self.get_user(user_id)
            for user_id in (contributor_ids or [])
        ]

        task = Task(title, project, contributors)
        project.add_task(task)
        self.tasks.append(task)
        self.save()
        return task

    def get_user(self, user_id):
        """Find a user by ID."""
        for user in self.users:
            if user.id == user_id:
                return user
        raise ValueError(f"No user found with ID {user_id}.")

    def get_project(self, project_id):
        """Find a project by ID."""
        for project in self.projects:
            if project.id == project_id:
                return project
        raise ValueError(f"No project found with ID {project_id}.")

    def get_task(self, task_id):
        """Find a task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"No task found with ID {task_id}.")

    def complete_task(self, task_id):
        """Mark a task complete and persist the change."""
        task = self.get_task(task_id)
        task.mark_complete()
        self.save()
        return task
