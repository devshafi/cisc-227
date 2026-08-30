# Instructor / TA Notes (do not distribute to students)

## Intentional gaps and bugs

All three reference apps are deliberately incomplete/buggy to support later assignments
(A2 requirements-vs-implementation gap analysis; A3 unit testing, mocking, coverage).
The third project (Equipment Rental Management) was added 2026-08-30 to spread 180+
students' groups across three domains instead of two.

### Missing features (by design, not bugs)

- **LMS**: no Reservation/Hold, no Overdue Fine calculation. Stakeholder role cards
  in `assignment-1/library-management/role_cards/` ask for these, so students should
  surface them as unmet requirements in Assignment 2.
- **IMS**: no Purchase Order, no low-stock reorder alert. Role cards in
  `assignment-1/inventory-management/role_cards/` ask for these similarly.
- **ERM**: no damage-deposit tracking, no maintenance/out-of-service flag for equipment
  under repair. Role cards in `assignment-1/equipment-rental-management/role_cards/`
  ask for these similarly.

### Planted bugs (2 per project, mirrored)

**Library Management — `projects/library-management/app/routes/loans.py`**
1. `checkout_book()` decrements `available_copies` without checking it is `> 0` first,
   so a book can be checked out more times than copies exist (`available_copies` goes negative).
2. `list_loans()`: the `member_id` filter branch uses `l.book_id == member_id` instead of
   `l.member_id == member_id` (copy-paste bug from the `book_id` branch below it).

**Inventory Management — `projects/inventory-management/app/routes/transactions.py`**
1. `create_transaction()` decrements `quantity_on_hand` for an `OUT` transaction without
   checking sufficient stock first, so stock can go negative.
2. `list_transactions()`: the `product_id` filter branch uses `t.supplier_id == product_id`
   instead of `t.product_id == product_id` (copy-paste bug from the `supplier_id` branch below it).

**Equipment Rental Management — `projects/equipment-rental-management/app/routes/rentals.py`**
1. `checkout_equipment()` decrements `available_units` without checking it is `> 0` first,
   so equipment can be checked out more times than units exist (`available_units` goes negative).
2. `list_rentals()`: the `renter_id` filter branch uses `r.equipment_id == renter_id` instead of
   `r.renter_id == renter_id` (copy-paste bug from the `equipment_id` branch below it).

These bugs are intended to be caught by the unit tests students write in Assignment 2/3.
Do not fix them in the reference repos before those assignments are complete.

## Storage

All three apps store data as plain Python objects in module-level dicts
(`app/store.py`), not a database. Students cover databases later in the
program (per instructor request, 2026-08-30). Data resets whenever the app
restarts. Each `store.py` exposes a `reset()` helper for clearing state
between pytest tests, used by the `conftest.py` fixture described below.

## Environment

Each project is a standalone Flask app meant to run from its own `.venv`
(`python -m venv .venv`, see each project's README), not shared across
projects when handed out to students as separate repos. In this working
copy the three projects currently share one `.venv` under `projects/` for
convenience while developing; that is not how students will run them.

## Assignment 2 additions (2026-08-30)

- Each project's `tests/conftest.py` provides a `client` pytest fixture:
  a Flask test client wired to `create_app()`, with `store.reset()` called
  before and after every test so tests don't leak state into each other.
  This is the only scaffolding provided; students still write all the actual
  test functions themselves.
- `assignment-2/README.md`: student-facing instructions covering getting the
  project into their own repo, the branching workflow (per-member feature
  branches merged directly into `main` via pull request; the TA grades by
  running `main`), the requirements-vs-implementation comparison, and the
  pytest requirement (at least 2 tested functions per member, on functions
  confirmed to be implemented).
- `assignment-2/requirements_comparison_template.md`: the table template
  groups fill in against their Assignment 1 final requirements list. It
  deliberately asks a "did anything behave unexpectedly" question at the end
  to nudge groups toward the planted bugs without naming them outright.
- Repo delivery method for A2: groups clone the course repo, copy out just
  their chosen project's folder, and push it into the empty repo they
  created in Assignment 1's pre-work (no GitHub template repos used).
