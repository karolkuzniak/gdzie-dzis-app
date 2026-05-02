from flask import Blueprint, jsonify, request
from models import db, Event

bp = Blueprint("events", __name__)

@bp.route("/events", methods=["GET"])
def get_events():
    """
    Pobierz wszystkie wydarzenia
    ---
    responses:
      200:
        description: Lista wydarzen
    """
    events = Event.query.all()
    return jsonify([e.to_dict() for e in events])

@bp.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    """
    Pobierz jedno wydarzenie
    ---
    parameters:
      - name: event_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Szczegoly wydarzenia
      404:
        description: Nie znaleziono
    """
    event = Event.query.get_or_404(event_id)
    return jsonify(event.to_dict())

@bp.route("/events", methods=["POST"])
def add_event():
    """
    Dodaj nowe wydarzenie
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: Koncert Elektryczny
            city:
              type: string
              example: Wroclaw
            date:
              type: string
              example: "2026-06-01"
            description:
              type: string
              example: Swietny koncert w centrum
    responses:
      201:
        description: Wydarzenie dodane
    """
    data = request.json
    event = Event(
        title=data["title"],
        city=data["city"],
        date=data["date"],
        description=data.get("description", "")
    )
    db.session.add(event)
    db.session.commit()
    return jsonify(event.to_dict()), 201

@bp.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    """
    Usun wydarzenie
    ---
    parameters:
      - name: event_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Wydarzenie usuniete
      404:
        description: Nie znaleziono
    """
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "deleted"}), 200