# Project Management CLI Tool

A command-line project management application built with Python. It allows users to manage team members, projects, tasks, and task contributors, with data saved in a JSON file.

## Features

- **Object-oriented design:** Uses `Person`, `User`, `Project`, and `Task` classes.
- **User management:** Create and list users.
- **Project management:** Create projects with descriptions, due dates, and owners.
- **Task management:** Create and list tasks, assign multiple contributors, and mark tasks as complete.
- **JSON persistence:** Saves records to a local JSON database and restores them when the application restarts.
- **Input validation:** Handles duplicate user emails, invalid references, and invalid task statuses.
- **Automated tests:** Uses pytest to test models, manager functionality, and CLI commands.

## Requirements

- Python 3.12 or a compatible Python 3 version.
- pip.
- A terminal.

## Installation

1. Clone or download this repository.
2. Navigate into the project directory.
3. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run commands from the project root directory.

### Display available commands

```bash
python main.py --help
```

### Add a user

```bash
python main.py add-user --name Hanifa --email hanifah52@gmail.com
```

### List users

```bash
python main.py list-users
```

### Add a project

The owner ID must belong to an existing user.

```bash
python main.py add-project \
  --title "Clothing Collection Design" \
  --description "Design the first clothing collection" \
  --due-date 2026-12-31 \
  --owner-id 1
```

Dates must use the `YYYY-MM-DD` format.

### List projects

```bash
python main.py list-projects
```

### Add a task

The project ID must exist. Contributor IDs are optional and must belong to existing users.

```bash
python main.py add-task \
  --title "Finalize garment sketches" \
  --project-id 1 \
  --contributors 1 2
```

### List tasks

```bash
python main.py list-tasks
```

### Mark a task complete

```bash
python main.py complete-task --task-id 1
```

## Running the tests

Install the dependencies, activate the virtual environment, and run:

```bash
pytest -v
```

The test suite covers model behavior, manager validation, persistence, and CLI commands.

## Project structure

```text
project-management-cli/
├── main.py
├── manager.py
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   └── task.py
├── utils/
│   ├── __init__.py
│   └── storage.py
├── data/
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_manager.py
│   └── test_cli.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Data storage

Application data is stored in `data/database.json`. The application creates the data file and its parent directory when needed. Back up this file if you need to preserve your records.

## Limitations

- Data is stored locally in JSON rather than in a database server.
- The application is designed for command-line use; it does not include a graphical interface.
- User authentication and multi-user access control are not implemented.

## Technologies

- Python
- Object-oriented programming
- `argparse`
- JSON
- `pytest`

## License

No license has been selected yet. Add a license before distributing or reusing this project publicly.
