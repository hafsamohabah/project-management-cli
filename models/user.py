
"""Define the User class for the project management application."""

from models.person import Person


class User(Person):
    """Represent an application user who can own projects."""

    _next_id = 1

    def __init__(self, name, email):
        """Initialize a user with a unique ID, name, and email."""
        super().__init__(name, email)

        self._id = User._next_id
        User._next_id += 1

        self._projects = []

    @property
    def id(self):
        """Return the user's unique ID."""
        return self._id

    @property
    def projects(self):
        """Return a copy of the user's project collection."""
        return self._projects.copy()

    def add_project(self, project):
        """Add a project if this user owns it."""
        if project.owner is not self:
            raise ValueError(
                "This project belongs to another user."
            )

        if project not in self._projects:
            self._projects.append(project)

    def __str__(self):
        """Return a readable description of the user."""
        return f"User {self._id}: {self.name} ({self.email})"

    def __repr__(self):
        """Return a representation useful for debugging."""
        return (
            f"User(id={self.id!r}, "
            f"name={self.name!r}, "
            f"email={self.email!r})"
        )
