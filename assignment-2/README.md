# Assignment 2: Environment Setup, Requirements Verification, and Unit Testing

## Overview

In this assignment, you will get the reference application for your chosen
project (Library Management, Inventory Management, or Equipment Rental
Management) running on your own machines, bring it into the GitHub repo your
group created in Assignment 1, and start working on it as a team using
feature branches. You will then check how many of the requirements from your
Assignment 1 final list are actually implemented by the running application,
and write unit tests (using pytest) for the functions that are implemented.

## Steps

### 1. Get the project into your repo

1. Clone the course repository (link provided separately) to a temporary
   location on your machine.
2. Copy only your group's chosen project folder (for example
   `library-management/`) out of that clone. Do not include the other two
   projects.
3. Remove any leftover git history from the copy (there shouldn't be a
   `.git/` folder inside the project folder itself; if there is, delete it).
4. Inside the empty GitHub repo your group created in Assignment 1's
   pre-work, add this project folder's contents at the top level and push
   your first commit.

```bash
git clone <course-repo-url> temp-course-clone
cp -r temp-course-clone/library-management/. path/to/your-group-repo/
cd path/to/your-group-repo
git add .
git commit -m "Add starting project code"
git push origin main
```

(Substitute `library-management` for `inventory-management` or
`equipment-rental-management` if that's your group's project.)

### 2. Set up your local environment

Each member, on their own machine:

```bash
cd your-group-repo
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Confirm the app runs at `http://127.0.0.1:5000` and that you can use the
basic web UI (`/`) as well as the JSON API endpoints listed in the project's
`README.md`.

### 3. Branching workflow

1. Each member creates their own branch off `main` (for example
   `feature/alice-tests`, `feature/bob-tests`).
2. Do your work (Steps 4 and 5 below) on your own branch, committing as you
   go.
3. When your work is ready, open a pull request back into `main`. Have your
   partner review and approve it before merging.
4. By the end of the assignment, `main` should contain both members' work,
   merged cleanly. Your TA will run `main` to grade this assignment, so make
   sure it's up to date and the app still runs from it before you submit.

### 4. Requirements-vs-implementation comparison

Take your group's final requirements list from Assignment 1. For every
requirement, run the application (using the web UI, curl, or Postman) and
determine whether it is actually implemented. Use the table template in
[requirements_comparison_template.md](requirements_comparison_template.md)
and classify each requirement as:

- **Implemented**: the running app fully satisfies it.
- **Partially implemented**: some of it works, but part is missing or wrong.
- **Not implemented**: there's no corresponding functionality in the app.

For each entry, note what you actually did to test it (the request you sent,
the button you clicked, the response you got) as evidence. You are expected
to find gaps: some requirements from your role-play (especially the ones
tied to features stakeholders wanted) will not be implemented at all. That's
the point of this exercise, not a mistake in the reference app.

### 5. Unit testing with pytest

The project's `tests/` folder already contains a `conftest.py` with a
`client` fixture: a Flask test client, wired up so the in-memory data store
is reset before and after every test. You can use it directly:

```python
def test_list_books_starts_empty(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert response.get_json() == []
```

**Each member must write pytest tests for at least 2 different functions**
(route handlers or model methods) that your comparison in Step 4 confirmed
are actually implemented. Do not write tests for missing features. Pick
functions you think are worth testing, not just the easiest ones; a test
that never fails because it barely checks anything doesn't count for much.
Put your tests in their own file (for example `tests/test_<yourname>.py`) on
your own branch.

Run your tests locally before opening your pull request:

```bash
pytest
```

## Deliverables

1. GitHub repo with the project code, `main` branch containing both members'
   merged work, and a visible commit history showing individual branches and
   pull requests. Your TA will run `main` to grade this assignment.
2. Requirements-vs-implementation comparison table (completed).
3. pytest test files (at least 2 functions per member, 4+ total for the
   group).
4. A short PDF submitted to OnQ containing: a link to your GitHub repo, the
   completed comparison table, and a brief summary of which functions you
   each tested and why.

## Suggested grading scheme (out of 10)

| Component | Marks |
|---|---|
| Environment set up, app runs, project pushed to group repo | 1 |
| Branching workflow followed (individual branches, pull requests, `main` up to date and runnable) | 2 |
| Requirements-vs-implementation comparison (accuracy and completeness) | 3 |
| Unit tests (at least 2 meaningful functions per member) | 3 |
| Submission quality (PDF, repo link, organization) | 1 |
| **Total** | **10** |
