# Project Management CLI Tool

## About the Project

This is a Python command-line application for managing users, projects, and tasks. It was built to practise object-oriented programming, working with files, and using Python commands from the terminal.

Users can create projects, assign tasks to projects, add contributors to tasks, and mark tasks as complete. The application saves its data in a JSON file so that records can be loaded again when the program is run.

## Features

- Create and list users.
- Create projects with titles, descriptions, due dates, and owners.
- Create and list tasks.
- Assign multiple contributors to a task.
- Mark tasks as complete.
- Save and load application data using JSON.
- Validate project titles, task titles, task statuses, and user email uniqueness.
- Run automated tests using pytest.

## Technologies Used

- Python 3
- Object-oriented programming
- `argparse` for command-line arguments
- JSON for data storage
- `pytest` for automated testing

## Requirements

- Python 3.12 or a compatible version.
- pip

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hafsamohabah/project-management-cli.git
   ```

2. Navigate to the project directory:

   ```bash
   cd project-management-cli
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

4. Activate the virtual environment on Linux or WSL Ubuntu:

   ```bash
   source .venv/bin/activate
   ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

Run the commands from the project directory.

### View available commands

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

The due date must use the `YYYY-MM-DD` format.

### List projects

```bash
python main.py list-projects
```

### Add a task

The project ID must belong to an existing project. Contributor IDs are optional.

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

### Complete a task

```bash
python main.py complete-task --task-id 1
```

## Running the Tests

With the virtual environment activated, run:

```bash
pytest -v
```

The tests check the model classes, project management operations, data persistence, and command-line behavior.

## Project Structure

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

Two additional scripts, `test_person.py` and `test_storage.py`, are included for manual testing.

## Data Storage

The application stores users, projects, and tasks in `data/database.json`. It uses IDs to link projects to their owners and tasks to their projects and contributors.

The local database is excluded from Git, so each installation can create its own data file.

## Limitations

- Data is stored in a local JSON file rather than a database server.
- The application runs in the terminal and does not have a graphical interface.
- User authentication and access control are not implemented.

## Repository

GitHub: https://github.com/hafsamohabah/project-management-cli
