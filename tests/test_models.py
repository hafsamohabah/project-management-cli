
"""Test the core project management models."""

import pytest

from models.person import Person
from models.user import User
from models.project import Project
from models.task import Task


def test_person_stores_name_and_email():
    person = Person("Hanifa", "hanifah52@gmail.com")

    assert person.name == "Hanifa"
    assert person.email == "hanifah52@gmail.com"


def test_person_string_representations():
    person = Person("Hanifa", "hanifah52@gmail.com")

    assert str(person) == "Hanifa (hanifah52@gmail.com)"
    assert "Person(name=" in repr(person)


def test_user_inherits_from_person():
    user = User("Hanifa", "hanifah52@gmail.com")

    assert isinstance(user, Person)
    assert user.name == "Hanifa"


def test_user_repr_contains_user_details():
    user = User("Hanifa", "hanifah52@gmail.com")

    assert "User(id=" in repr(user)
    assert "Hanifa" in repr(user)


def test_project_rejects_empty_title():
    user = User("Hanifa", "hanifah52@gmail.com")

    with pytest.raises(ValueError):
        Project("", "A description", "2026-12-31", user)


def test_project_repr_contains_project_details():
    user = User("Hanifa", "hanifah52@gmail.com")
    project = Project(
        "Clothing Collection",
        "Design a clothing collection",
        "2026-12-31",
        user,
    )

    assert "Project(id=" in repr(project)
    assert "Clothing Collection" in repr(project)


def test_task_starts_as_pending():
    user = User("Hanifa", "hanifah52@gmail.com")
    project = Project(
        "Clothing Collection",
        "Design a clothing collection",
        "2026-12-31",
        user,
    )
    task = Task("Draw garment sketches", project)

    assert task.status == "Pending"


def test_task_can_be_completed():
    user = User("Hanifa", "hanifah52@gmail.com")
    project = Project(
        "Clothing Collection",
        "Design a clothing collection",
        "2026-12-31",
        user,
    )
    task = Task("Draw garment sketches", project)

    task.mark_complete()

    assert task.status == "Complete"


def test_task_rejects_invalid_status():
    user = User("Hanifa", "hanifah52@gmail.com")
    project = Project(
        "Clothing Collection",
        "Design a clothing collection",
        "2026-12-31",
        user,
    )
    task = Task("Draw garment sketches", project)

    with pytest.raises(ValueError):
        task.status = "Started"


def test_task_can_have_multiple_contributors():
    hanifa = User("Hanifa", "hanifah52@gmail.com")
    jeff = User("Jeff", "jeff@gmail.com")
    project = Project(
        "Clothing Collection",
        "Design a clothing collection",
        "2026-12-31",
        hanifa,
    )
    task = Task(
        "Draw garment sketches",
        project,
        contributors=[hanifa, jeff],
    )

    assert len(task.contributors) == 2
    assert hanifa in task.contributors
    assert jeff in task.contributors


def test_task_repr_contains_task_details():
    user = User("Hanifa", "hanifah52@gmail.com")
    project = Project(
        "Clothing Collection",
        "Design a clothing collection",
        "2026-12-31",
        user,
    )
    task = Task("Draw garment sketches", project)

    representation = repr(task)

    assert "Task(id=" in representation
    assert "Draw garment sketches" in representation
    assert "Pending" in representation

def test_project_rejects_invalid_due_date():
    user = User("Hanifa", "hanifah52@gmail.com")

    with pytest.raises(ValueError, match="YYYY-MM-DD"):
        Project(
            "Clothing Collection",
            "Design a clothing collection",
            "tomorrow",
            user,
        )
