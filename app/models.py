from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "city": self.city,
            "date": self.date,
            "description": self.description
        }

