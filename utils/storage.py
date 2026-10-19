
"""Provide JSON file storage utilities for the application."""

import json
from pathlib import Path


DEFAULT_DATA = {
    "users": [],
    "projects": [],
    "tasks": [],
}


def load_data(file_path):
    """Load application data from a JSON file.

    Return an empty data structure if the file does not exist.
    Raise a helpful error if the JSON is malformed or unreadable.
    """
    path = Path(file_path)

    if not path.exists():
        return {
            "users": [],
            "projects": [],
            "tasks": [],
        }

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"The JSON file is malformed: {path}"
        ) from error

    except OSError as error:
        raise OSError(
            f"Could not read the data file: {path}"
        ) from error

    if not isinstance(data, dict):
        raise ValueError("The data file must contain a JSON object.")

    for key in DEFAULT_DATA:
        if key not in data:
            data[key] = []

        if not isinstance(data[key], list):
            raise ValueError(
                f"The '{key}' section must contain a list."
            )

    return data


def save_data(data, file_path):
    """Save application data to a JSON file.

    Create the parent directory if it does not exist.
    """
    path = Path(file_path)

    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary.")

    for key in DEFAULT_DATA:
        if key not in data or not isinstance(data[key], list):
            raise ValueError(
                f"Data must contain a list named '{key}'."
            )

    try:
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    except OSError as error:
        raise OSError(
            f"Could not save the data file: {path}"
        ) from error
