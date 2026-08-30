from flask import Blueprint, jsonify, request

from app import store
from app.models.supplier import Supplier

suppliers_bp = Blueprint("suppliers", __name__, url_prefix="/suppliers")


@suppliers_bp.route("", methods=["GET"])
def list_suppliers():
    return jsonify([s.to_dict() for s in store.suppliers.values()])


@suppliers_bp.route("", methods=["POST"])
def create_supplier():
    data = request.get_json()
    supplier_id = store.next_id("supplier")
    supplier = Supplier(id=supplier_id, name=data["name"], contact_email=data["contact_email"])
    store.suppliers[supplier_id] = supplier
    return jsonify(supplier.to_dict()), 201


@suppliers_bp.route("/<int:supplier_id>", methods=["GET"])
def get_supplier(supplier_id):
    supplier = store.suppliers.get(supplier_id)
    if supplier is None:
        return jsonify({"error": "Supplier not found"}), 404
    return jsonify(supplier.to_dict())


@suppliers_bp.route("/<int:supplier_id>", methods=["PUT"])
def update_supplier(supplier_id):
    supplier = store.suppliers.get(supplier_id)
    if supplier is None:
        return jsonify({"error": "Supplier not found"}), 404
    data = request.get_json()
    supplier.name = data.get("name", supplier.name)
    supplier.contact_email = data.get("contact_email", supplier.contact_email)
    return jsonify(supplier.to_dict())


@suppliers_bp.route("/<int:supplier_id>", methods=["DELETE"])
def delete_supplier(supplier_id):
    supplier = store.suppliers.pop(supplier_id, None)
    if supplier is None:
        return jsonify({"error": "Supplier not found"}), 404
    return "", 204
