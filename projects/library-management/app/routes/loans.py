from datetime import date

from flask import Blueprint, jsonify, request

from app import store
from app.models.loan import Loan

loans_bp = Blueprint("loans", __name__, url_prefix="/loans")


@loans_bp.route("", methods=["GET"])
def list_loans():
    results = list(store.loans.values())
    member_id = request.args.get("member_id", type=int)
    book_id = request.args.get("book_id", type=int)
    if member_id is not None:
        results = [l for l in results if l.book_id == member_id]
    if book_id is not None:
        results = [l for l in results if l.book_id == book_id]
    return jsonify([l.to_dict() for l in results])


@loans_bp.route("", methods=["POST"])
def checkout_book():
    data = request.get_json()
    book = store.books.get(data["book_id"])
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    book.available_copies -= 1

    loan_id = store.next_id("loan")
    loan = Loan(
        id=loan_id,
        book_id=data["book_id"],
        member_id=data["member_id"],
        due_date=Loan.default_due_date(),
    )
    store.loans[loan_id] = loan
    return jsonify(loan.to_dict()), 201


@loans_bp.route("/<int:loan_id>/return", methods=["PUT"])
def return_book(loan_id):
    loan = store.loans.get(loan_id)
    if loan is None:
        return jsonify({"error": "Loan not found"}), 404
    if loan.return_date is not None:
        return jsonify({"error": "Loan already returned"}), 400

    loan.return_date = date.today()
    book = store.books.get(loan.book_id)
    book.available_copies += 1

    return jsonify(loan.to_dict())
