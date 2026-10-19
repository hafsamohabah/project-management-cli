
"""Define the Task class."""

from models.user import User


class Task:
    """Represent a task belonging to a project."""

    _next_id = 1
    VALID_STATUSES = ("Pending", "In Progress", "Complete")

    def __init__(self, title, project, contributors=None):
        """Initialize a task with a project and optional contributors."""
        self._id = Task._next_id
        Task._next_id += 1

        self.title = title
        self.project = project
        self._status = "Pending"
        self._contributors = []

        if contributors:
            for contributor in contributors:
                self.add_contributor(contributor)

    @property
    def id(self):
        """Return the task's unique ID."""
        return self._id

    @property
    def title(self):
        """Return the task's title."""
        return self._title

    @title.setter
    def title(self, value):
        """Set the title after validating that it is not empty."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Task title cannot be empty.")

        self._title = value.strip()

    @property
    def status(self):
        """Return the current task status."""
        return self._status

    @status.setter
    def status(self, value):
        """Set the status only if it is a recognized status."""
        if value not in self.VALID_STATUSES:
            raise ValueError(
                f"Invalid status. Choose from: {self.VALID_STATUSES}"
            )

        self._status = value

    @property
    def contributors(self):
        """Return a copy of the task's contributors."""
        return self._contributors.copy()

    def add_contributor(self, user):
        """Add a user who contributes to this task."""
        if not isinstance(user, User):
            raise TypeError("A contributor must be a User object.")

        if user not in self._contributors:
            self._contributors.append(user)

    def mark_complete(self):
        """Mark the task as complete."""
        self.status = "Complete"

    def __str__(self):
        """Return a readable summary of the task."""
        contributor_names = ", ".join(
            user.name for user in self._contributors
        )

        return (
            f"Task {self._id}: {self.title} | "
            f"Status: {self.status} | "
            f"Project: {self.project.title} | "
            f"Contributors: {contributor_names or 'None'}"
        )

    def __repr__(self):
        """Return a representation useful for debugging."""
        contributor_ids = [
            user.id for user in self._contributors
        ]

        return (
            f"Task(id={self.id!r}, "
            f"title={self.title!r}, "
            f"status={self.status!r}, "
            f"project_id={self.project.id!r}, "
            f"contributor_ids={contributor_ids!r})"
        )
