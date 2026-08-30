from flask import Blueprint, jsonify, request

from app import store
from app.models.equipment import Equipment

equipment_bp = Blueprint("equipment", __name__, url_prefix="/equipment")


@equipment_bp.route("", methods=["GET"])
def list_equipment():
    return jsonify([e.to_dict() for e in store.equipment.values()])


@equipment_bp.route("", methods=["POST"])
def create_equipment():
    data = request.get_json()
    equipment_id = store.next_id("equipment")
    item = Equipment(
        id=equipment_id,
        name=data["name"],
        category=data["category"],
        total_units=data.get("total_units", 1),
        available_units=data.get("total_units", 1),
    )
    store.equipment[equipment_id] = item
    return jsonify(item.to_dict()), 201


@equipment_bp.route("/<int:equipment_id>", methods=["GET"])
def get_equipment(equipment_id):
    item = store.equipment.get(equipment_id)
    if item is None:
        return jsonify({"error": "Equipment not found"}), 404
    return jsonify(item.to_dict())


@equipment_bp.route("/<int:equipment_id>", methods=["PUT"])
def update_equipment(equipment_id):
    item = store.equipment.get(equipment_id)
    if item is None:
        return jsonify({"error": "Equipment not found"}), 404
    data = request.get_json()
    item.name = data.get("name", item.name)
    item.category = data.get("category", item.category)
    item.total_units = data.get("total_units", item.total_units)
    item.available_units = data.get("available_units", item.available_units)
    return jsonify(item.to_dict())


@equipment_bp.route("/<int:equipment_id>", methods=["DELETE"])
def delete_equipment(equipment_id):
    item = store.equipment.pop(equipment_id, None)
    if item is None:
        return jsonify({"error": "Equipment not found"}), 404
    return "", 204
