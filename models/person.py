
"""Define the base Person class."""


class Person:
    """Represent a person with a name and email address."""

    def __init__(self, name, email):
        """Initialize a person with a name and email."""
        self.name = name
        self.email = email

    def __str__(self):
        """Return a readable description of the person."""
        return f"{self.name} ({self.email})"

    def __repr__(self):
        """Return a representation useful for debugging."""
        return (
            f"Person(name={self.name!r}, "
            f"email={self.email!r})"
        )
