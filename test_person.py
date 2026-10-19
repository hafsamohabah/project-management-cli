
"""Test users, projects, tasks, and contributors."""

from models.person import Person
from models.user import User
from models.project import Project
from models.task import Task


def main():
    """Create and test a clothing-brand project management scenario."""

    # Create people.
    print("=== PEOPLE ===")
    print(Person("Hanifa", "hanifah52@gmail.com"))
    print(Person("Jeff", "jeff@gmail.com"))
    print(Person("Zackary", "zackary33@gmail.com"))

    # Create users.
    print("\n=== USERS ===")
    hanifa = User("Hanifa", "hanifah52@gmail.com")
    jeff = User("Jeff", "jeff@gmail.com")
    zackary = User("Zackary", "zackary33@gmail.com")

    print(hanifa)
    print(jeff)
    print(zackary)

    # Create clothing-brand projects.
    print("\n=== PROJECTS ===")

    clothing_design = Project(
        "Clothing Collection Design",
        "Design the first clothing collection",
        "2026-12-31",
        hanifa,
    )

    branding = Project(
        "Branding and Packaging",
        "Develop the brand identity and packaging",
        "2027-01-31",
        jeff,
    )

    production = Project(
        "Production Planning",
        "Plan fabric sourcing and garment production",
        "2027-02-28",
        zackary,
    )

    hanifa.add_project(clothing_design)
    jeff.add_project(branding)
    zackary.add_project(production)

    print(clothing_design)
    print(branding)
    print(production)

    # Create tasks.
    print("\n=== TASKS ===")

    task1 = Task(
        "Finalize garment sketches",
        clothing_design,
        contributors=[hanifa, jeff],
    )

    task2 = Task(
        "Select fabrics and colors",
        clothing_design,
        contributors=[hanifa, zackary],
    )

    task3 = Task(
        "Design clothing labels",
        branding,
        contributors=[jeff, zackary],
    )

    # Register tasks with their projects.
    clothing_design.add_task(task1)
    clothing_design.add_task(task2)
    branding.add_task(task3)

    print(task1)
    print(task2)
    print(task3)

    # Show the tasks in Hanifa's project.
    print("\n=== CLOTHING COLLECTION TASKS ===")
    for task in clothing_design.tasks:
        print(task.title, "-", task.status)

    # Mark a task as complete.
    print("\n=== COMPLETE A TASK ===")
    task1.mark_complete()
    print(task1)

    # Display the updated status.
    print("\nUpdated status:", task1.status)


if __name__ == "__main__":
    main()
