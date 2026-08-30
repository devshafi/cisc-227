from datetime import date

from flask import Blueprint, jsonify, request

from app import store
from app.models.rental import Rental

rentals_bp = Blueprint("rentals", __name__, url_prefix="/rentals")


@rentals_bp.route("", methods=["GET"])
def list_rentals():
    results = list(store.rentals.values())
    renter_id = request.args.get("renter_id", type=int)
    equipment_id = request.args.get("equipment_id", type=int)
    if renter_id is not None:
        results = [r for r in results if r.equipment_id == renter_id]
    if equipment_id is not None:
        results = [r for r in results if r.equipment_id == equipment_id]
    return jsonify([r.to_dict() for r in results])


@rentals_bp.route("", methods=["POST"])
def checkout_equipment():
    data = request.get_json()
    item = store.equipment.get(data["equipment_id"])
    if item is None:
        return jsonify({"error": "Equipment not found"}), 404

    item.available_units -= 1

    rental_id = store.next_id("rental")
    rental = Rental(
        id=rental_id,
        equipment_id=data["equipment_id"],
        renter_id=data["renter_id"],
        due_date=Rental.default_due_date(),
    )
    store.rentals[rental_id] = rental
    return jsonify(rental.to_dict()), 201


@rentals_bp.route("/<int:rental_id>/return", methods=["PUT"])
def return_equipment(rental_id):
    rental = store.rentals.get(rental_id)
    if rental is None:
        return jsonify({"error": "Rental not found"}), 404
    if rental.return_date is not None:
        return jsonify({"error": "Rental already returned"}), 400

    rental.return_date = date.today()
    item = store.equipment.get(rental.equipment_id)
    if item is not None:
        item.available_units += 1

    return jsonify(rental.to_dict())
