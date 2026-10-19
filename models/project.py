
"""Define the Project class."""

from datetime import date

from models.user import User


class Project:
    """Represent a project owned by a user."""

    _next_id = 1

    def __init__(self, title, description, due_date, owner):
        """Initialize a project and its relationship to its owner."""
        self._id = Project._next_id
        Project._next_id += 1

        self.title = title
        self.description = description

        if isinstance(due_date, str):
            try:
                due_date = date.fromisoformat(due_date)
            except ValueError as error:
                raise ValueError(
                    "Due date must use YYYY-MM-DD format."
                ) from error

        if not isinstance(due_date, date):
            raise TypeError(
                "Due date must be a date or ISO date string."
            )

        self.due_date = due_date
        self.owner = owner
        self._tasks = []

    @property
    def id(self):
        """Return the project's unique ID."""
        return self._id

    @property
    def title(self):
        """Return the project's title."""
        return self._title

    @title.setter
    def title(self, value):
        """Set the title after checking that it is not empty."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Project title cannot be empty.")

        self._title = value.strip()

    @property
    def tasks(self):
        """Return a copy of the project's task collection."""
        return self._tasks.copy()

    def add_task(self, task):
        """Add a task belonging to this project."""
        if task.project is not self:
            raise ValueError("This task belongs to another project.")

        if task not in self._tasks:
            self._tasks.append(task)

    def __str__(self):
        """Return a readable summary of the project."""
        return (
            f"Project {self._id}: {self.title} | "
            f"Owner: {self.owner.name} | "
            f"Due: {self.due_date}"
        )

    def __repr__(self):
        """Return a representation useful for debugging."""
        return (
            f"Project(id={self.id!r}, "
            f"title={self.title!r}, "
            f"due_date={self.due_date!r}, "
            f"owner_id={self.owner.id!r})"
        )
