
"""Command-line interface for the project management application."""

import argparse
import sys

from manager import ProjectManager


def build_parser():
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Manage users, projects, and tasks."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    # Add user command.
    add_user_parser = subparsers.add_parser(
        "add-user",
        help="Create a new user.",
    )
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)

    # List users command.
    subparsers.add_parser(
        "list-users",
        help="Display all users.",
    )

    # Add project command.
    add_project_parser = subparsers.add_parser(
        "add-project",
        help="Create a project.",
    )
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.add_argument(
        "--due-date",
        required=True,
        help="Due date in YYYY-MM-DD format.",
    )
    add_project_parser.add_argument(
        "--owner-id",
        required=True,
        type=int,
    )

    # List projects command.
    subparsers.add_parser(
        "list-projects",
        help="Display all projects.",
    )

    # Add task command.
    add_task_parser = subparsers.add_parser(
        "add-task",
        help="Create a task for a project.",
    )
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument(
        "--project-id",
        required=True,
        type=int,
    )
    add_task_parser.add_argument(
        "--contributors",
        nargs="*",
        type=int,
        default=[],
        help="Optional contributor user IDs.",
    )

    # List tasks command.
    subparsers.add_parser(
        "list-tasks",
        help="Display all tasks.",
    )

    # Complete task command.
    complete_parser = subparsers.add_parser(
        "complete-task",
        help="Mark a task as complete.",
    )
    complete_parser.add_argument(
        "--task-id",
        required=True,
        type=int,
    )

    return parser


def main():
    """Parse a command and execute the requested operation."""
    parser = build_parser()
    args = parser.parse_args()

    manager = ProjectManager()

    try:
        if args.command == "add-user":
            user = manager.add_user(args.name, args.email)
            print(f"User created successfully: {user}")

        elif args.command == "list-users":
            if not manager.users:
                print("No users found.")
            else:
                for user in manager.users:
                    print(user)

        elif args.command == "add-project":
            project = manager.add_project(
                args.title,
                args.description,
                args.due_date,
                args.owner_id,
            )
            print(f"Project created successfully: {project}")

        elif args.command == "list-projects":
            if not manager.projects:
                print("No projects found.")
            else:
                for project in manager.projects:
                    print(project)

        elif args.command == "add-task":
            task = manager.add_task(
                args.title,
                args.project_id,
                args.contributors,
            )
            print(f"Task created successfully: {task}")

        elif args.command == "list-tasks":
            if not manager.tasks:
                print("No tasks found.")
            else:
                for task in manager.tasks:
                    print(task)

        elif args.command == "complete-task":
            task = manager.complete_task(args.task_id)
            print(f"Task marked complete: {task}")

    except (ValueError, TypeError, OSError, KeyError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
