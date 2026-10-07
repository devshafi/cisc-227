# Assignment 2: Environment Setup, Requirements Verification, and Unit Testing

## Overview

In this assignment, you will get the reference application for your chosen
project (Library Management, Inventory Management, or Equipment Rental
Management) running on your own machines, bring it into the GitHub repo your
group created in Assignment 1, and start working on it as a team using
feature branches. You will then verify how well the running application
matches the requirements your group elicited in Assignment 1, and write unit
tests (using pytest) that confirm — or challenge — your findings.

The reference app is intended to be feature-complete. Your job is not to find
what is missing: it is to verify that what is there actually behaves the way
your requirements say it should. Some things may not hold up under careful
testing. That's the point of this exercise.

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

For each entry, note what you actually did to check it: the request you sent,
the button you clicked, the response you got. Go beyond the happy path —
think about edge cases and sequences of operations your requirements imply.
Does the app handle unusual inputs the way your requirement says it should?
Does a multi-step workflow (e.g. create, then act on what you created) leave
the system in the state you expect? Discrepancies between expected and actual
behaviour — even when a feature appears to exist — are worth documenting, and
are what your tests in Step 5 should target.

### 5. Unit testing with pytest

The project's `tests/` folder contains a `conftest.py` and a `test_examples.py`
file. Read `test_examples.py` first — it shows two test patterns you will use
throughout this assignment:

1. **Empty-list check**: confirm an endpoint returns an empty list before any
   data is added.
2. **Create-then-verify**: POST something, then GET or act on it and assert
   the result matches what you expect.

These example tests are scaffolding. **Do not count them toward your required
test functions** — write your own in a new file (e.g. `tests/test_<yourname>.py`).

**Each member must write pytest tests for at least 2 different functions** on
their own branch. Choose functions that your Step 4 comparison confirmed are
implemented, and test beyond the happy path. A test that calls one endpoint
with valid input and checks only the HTTP status code is not sufficient on its
own. Good tests check what the data looks like after an operation, what
happens when you chain two operations together, and what happens at boundaries
(e.g. what if the thing you're acting on doesn't exist? what if a quantity is
at its limit?).

Run your tests locally before opening your pull request:

```bash
pytest
```

## Deliverables

1. GitHub repo with the project code, `main` branch containing both members'
   merged work, and a visible commit history showing individual branches and
   pull requests. Your TA will run `main` to grade this assignment.
2. Requirements-vs-implementation comparison table (completed), with evidence
   for each row (what you sent, what you got back).
3. pytest test files (at least 2 functions per member, 4+ total for the
   group), in your own named files under `tests/`.
4. A short PDF submitted to OnQ containing: a link to your GitHub repo, the
   completed comparison table, and a brief summary of which functions you
   each tested, why you chose them, and what your tests revealed.

## Grading Scheme

| Component | Marks |
|---|---|
| Environment set up, app runs, project pushed to group repo | 1 |
| Branching workflow followed (individual branches, pull requests, `main` up to date and runnable) | 2 |
| Requirements-vs-implementation comparison (accuracy, evidence, edge cases noted) | 2 |
| Unit tests (at least 2 meaningful functions per member, including edge-case or multi-step scenarios) | 4 |
| Submission quality (PDF, repo link, organization) | 1 |
| **Total** | **10** |
