
"""Test the command-line interface."""

import subprocess
import sys


def run_command(*arguments):
    """Run main.py and capture its output."""
    return subprocess.run(
        [sys.executable, "main.py", *arguments],
        capture_output=True,
        text=True,
        check=False,
    )


def test_help_command_succeeds():
    result = run_command("--help")

    assert result.returncode == 0
    assert "add-user" in result.stdout
    assert "list-projects" in result.stdout
    assert "complete-task" in result.stdout


def test_list_users_command_succeeds():
    result = run_command("list-users")

    assert result.returncode == 0
    assert "Error:" not in result.stderr


def test_missing_required_arguments_are_rejected():
    result = run_command("add-user")

    assert result.returncode != 0
    assert "--name" in result.stderr
    assert "--email" in result.stderr


def test_unknown_command_is_rejected():
    result = run_command("not-a-command")

    assert result.returncode != 0
    assert "invalid choice" in result.stderr.lower()
