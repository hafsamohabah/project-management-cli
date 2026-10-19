
"""Test project management and data persistence."""

import pytest

from manager import ProjectManager


def test_manager_adds_user(tmp_path):
    manager = ProjectManager(tmp_path / "database.json")

    user = manager.add_user(
        "Hanifa",
        "hanifah52@gmail.com",
    )

    assert user.name == "Hanifa"
    assert len(manager.users) == 1


def test_manager_rejects_duplicate_email(tmp_path):
    manager = ProjectManager(tmp_path / "database.json")

    manager.add_user("Hanifa", "hanifah52@gmail.com")

    with pytest.raises(ValueError, match="already exists"):
        manager.add_user("Another Hanifa", "HANIFAH52@gmail.com")


def test_manager_rejects_unknown_project_owner(tmp_path):
    manager = ProjectManager(tmp_path / "database.json")

    with pytest.raises(ValueError, match="No user found"):
        manager.add_project(
            "Clothing Collection",
            "Design the first collection",
            "2026-12-31",
            999,
        )


def test_manager_preserves_users_after_reload(tmp_path):
    file_path = tmp_path / "database.json"

    manager = ProjectManager(file_path)
    manager.add_user("Hanifa", "hanifah52@gmail.com")
    manager.add_user("Jeff", "jeff@gmail.com")

    reloaded_manager = ProjectManager(file_path)

    assert len(reloaded_manager.users) == 2
    assert reloaded_manager.get_user(1).name == "Hanifa"
    assert reloaded_manager.get_user(2).name == "Jeff"

def test_manager_reports_malformed_json(tmp_path):
    file_path = tmp_path / "database.json"
    file_path.write_text("{invalid json", encoding="utf-8")

    with pytest.raises(ValueError, match="malformed"):
        ProjectManager(file_path)


def test_manager_reports_project_with_unknown_owner(tmp_path):
    file_path = tmp_path / "database.json"
    file_path.write_text(
        '{"users": [], "projects": [{"id": 1}], "tasks": []}',
        encoding="utf-8",
    )

    with pytest.raises((ValueError, KeyError)):
        ProjectManager(file_path)
