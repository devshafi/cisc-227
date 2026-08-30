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

**Library Management — `library-management/app/routes/loans.py`**
1. `checkout_book()` decrements `available_copies` without checking it is `> 0` first,
   so a book can be checked out more times than copies exist (`available_copies` goes negative).
2. `list_loans()`: the `member_id` filter branch uses `l.book_id == member_id` instead of
   `l.member_id == member_id` (copy-paste bug from the `book_id` branch below it).

**Inventory Management — `inventory-management/app/routes/transactions.py`**
1. `create_transaction()` decrements `quantity_on_hand` for an `OUT` transaction without
   checking sufficient stock first, so stock can go negative.
2. `list_transactions()`: the `product_id` filter branch uses `t.supplier_id == product_id`
   instead of `t.product_id == product_id` (copy-paste bug from the `supplier_id` branch below it).

**Equipment Rental Management — `equipment-rental-management/app/routes/rentals.py`**
1. `checkout_equipment()` decrements `available_units` without checking it is `> 0` first,
   so equipment can be checked out more times than units exist (`available_units` goes negative).
2. `list_rentals()`: the `renter_id` filter branch uses `r.equipment_id == renter_id` instead of
   `r.renter_id == renter_id` (copy-paste bug from the `equipment_id` branch below it).

These bugs are intended to be caught by the unit tests students write in Assignment 2/3 —
do not fix them in the reference repos before those assignments are complete.

## Storage

All three apps store data as plain Python objects in module-level dicts
(`app/store.py`), not a database — students cover databases later in the
program (per instructor request, 2026-08-30). Data resets whenever the app
restarts. Each `store.py` exposes a `reset()` helper for clearing state
between pytest tests once students start writing them.

## Environment

Each project is a standalone Flask app meant to run from its own `.venv`
(`python -m venv .venv`, see each project's README) — not shared across
projects when handed out to students as separate repos.
