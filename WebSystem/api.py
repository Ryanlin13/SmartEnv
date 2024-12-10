from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)

@api_bp.route("/", methods=["GET"])
def api():
    return jsonify({"info":"hello world"})