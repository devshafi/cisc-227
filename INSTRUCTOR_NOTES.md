# Instructor / TA Notes (do not distribute to students)

## Intentional gaps and bugs

All three reference apps are deliberately incomplete/buggy to support later assignments
(A2 requirements-vs-implementation verification and unit testing; A3 unit testing,
mocking, coverage). The third project (Equipment Rental Management) was added
2026-08-30 to spread 180+ students' groups across three domains instead of two.

---

## A2 pivot (2026-08-31)

**Design change:** A2 was originally framed as a gap-analysis exercise (find missing
features). It has been reframed as a testing exercise: the apps are now feature-complete
relative to what students would elicit in A1, and the grade weight has shifted from
requirements comparison (3 marks) to unit testing (4 marks). Students are told the app
is "intended to be feature-complete" and that their job is to verify behaviour — some
things will not hold up under careful testing, but the frame is testing, not gap hunting.

---

## Features added per project (correct implementations)

### Library Management
- `GET /books?search=` — case-insensitive substring search on title and author
- `PUT /loans/<id>/renew` — extends due_date by LOAN_PERIOD_DAYS from the current due_date
- `POST /reservations` / `GET /reservations` — create and list reservations (book_id + member_id)
- `Reservation` model: `id, book_id, member_id, reservation_date, fulfilled`

### Inventory Management
- `reorder_level` field on `Product` (default 0); included in CRUD and `to_dict()`
- `GET /products/low-stock` — returns products where `quantity_on_hand <= reorder_level`
- `GET /suppliers/<id>/products` — returns products linked via IN transactions from that supplier
- `POST /purchase-orders` / `GET /purchase-orders` / `GET /purchase-orders/<id>` — create and list POs
- `PUT /purchase-orders/<id>/receive` — marks PO received (see bug below)
- `PurchaseOrder` model: `id, supplier_id, product_id, quantity_ordered, status, created_date, received_date`

### Equipment Rental Management
- `is_available` field on `Equipment` (default True); included in CRUD and `to_dict()`
- `PATCH /equipment/<id>/status` — set `is_available` True/False (out-of-service toggle)
- `GET /equipment/<id>/availability` — returns `is_available`, `available_units`, `total_units`
- `PUT /rentals/<id>/extend` — extends `due_date` by given number of days
- `deposit_amount` and `deposit_released` fields on `Rental` (defaults 0.0 / False)
- `PUT /rentals/<id>/deposit/release` — release deposit hold (see bug below)

---

## Intentional bugs — full inventory

### Original planted bugs (2 per project, unchanged)

**Library Management — `projects/library-management/app/routes/loans.py`**
1. `checkout_book()` decrements `available_copies` without checking `> 0` first.
2. `list_loans()`: `member_id` filter uses `l.book_id == member_id` (copy-paste from the `book_id` branch).

**Inventory Management — `projects/inventory-management/app/routes/transactions.py`**
1. `create_transaction()` decrements `quantity_on_hand` for OUT without checking sufficient stock.
2. `list_transactions()`: `product_id` filter uses `t.supplier_id == product_id` (copy-paste from the `supplier_id` branch).

**Equipment Rental Management — `projects/equipment-rental-management/app/routes/rentals.py`**
1. `checkout_equipment()` decrements `available_units` without checking `> 0` first.
2. `list_rentals()`: `renter_id` filter uses `r.equipment_id == renter_id` (copy-paste from the `equipment_id` branch).

Do not fix these before A2/A3 are complete.

---

### New bugs added 2026-08-31 (in newly added features)

**Library Management — 2 new bugs (4 total)**

3. `GET /loans/<id>/fine` (`loans.py`):
   Uses `date.today()` as the end date for fine calculation even when `loan.return_date`
   is set. A returned loan should cap its fine at the return date, but that branch is
   intentionally absent. A test that returns a book before its due date and then calls
   the fine endpoint will get a non-zero fine when the current date has passed the
   due_date — the fine keeps accruing even after return.
   *Student discovery path*: checkout a book with a past due_date, return it, call
   `GET /loans/<id>/fine` — expect $0.00 (returned before the test runs), get a
   growing positive amount.

4. `POST /loans` (`loans.py`) + `POST /reservations` (`reservations.py`):
   `checkout_book()` does not check `store.reservations` for pending reservations on
   the requested book. Any member can check out a book reserved by another member.
   *Student discovery path*: create a reservation for member A on book X, then check
   out book X as member B — expect failure or at minimum a warning, get 201 with the
   checkout succeeding silently.

**Inventory Management — 1 new bug (3 total)**

3. `PUT /purchase-orders/<id>/receive` (`purchase_orders.py`):
   Creates a Transaction record (type="IN") in `store.transactions` but does NOT
   update `product.quantity_on_hand`. The audit trail looks correct but the stock
   count stays unchanged.
   *Student discovery path*: create a product with quantity 10, create a PO for 50
   units, receive it, call `GET /products/<id>/stock-level` — expect 60, get 10.

**Equipment Rental Management — 2 new bugs (4 total)**

3. `PATCH /equipment/<id>/status` + `POST /rentals` (`equipment.py` / `rentals.py`):
   The status endpoint correctly sets `item.is_available = False`, but
   `checkout_equipment()` never checks this flag. Out-of-service equipment can still
   be rented.
   *Student discovery path*: mark equipment as `is_available: false`, attempt a
   checkout — expect a 400 error, get 201 with the rental created.

4. `PUT /rentals/<id>/deposit/release` (`rentals.py`):
   The response body includes `"deposit_released": true` but `rental.deposit_released`
   is never set to `True` on the object. A subsequent GET on the rental will show
   `"deposit_released": false`.
   *Student discovery path*: checkout with a deposit_amount, return the equipment,
   call the release endpoint (get `true` back), then GET the rental — see
   `deposit_released` is still `false`.

---

## Grading guidance for unit tests (A2)

Tests are worth 4/10 marks. The key distinction:

- **Shallow test** (max 2/4 for a group): calls one endpoint with valid data, checks
  only HTTP status code. e.g. `assert response.status_code == 201`.
- **Meaningful test** (full credit): checks the response body, chains multiple
  requests, or exercises a boundary/edge case. Students who write tests that expose
  any of the bugs above should receive full marks for those tests.

The example tests in `tests/test_examples.py` should not be counted — they are
clearly labelled as scaffolding. If a student submits only those two tests, treat it
as 0 student-authored functions.

---

## Example tests provided (scaffolding, not student work)

Each project's `tests/test_examples.py` has 2 tests:

| Project | Test 1 | Test 2 |
|---|---|---|
| LMS | `GET /books` returns `[]` initially | `POST /books` returns the created book |
| IMS | `GET /products` returns `[]` initially | `POST /products` + `GET /products/<id>/stock-level` |
| ERM | `GET /rentals` returns `[]` initially | `POST /equipment` + `GET /equipment/<id>/availability` |

---

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
