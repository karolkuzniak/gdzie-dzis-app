from flask import Flask, redirect
from models import db
from routes import bp
from flasgger import Swagger
import os


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/events_db"
)

#turn off unnecessary notifications
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Swagger UI conf
app.config["SWAGGER"] = {
    "title": "Gdzie dzis API",
    "description": "API do wyszukiwania i publikacji wydarzen",
    "version": "1.0.0"
}

db.init_app(app)
app.register_blueprint(bp)
Swagger(app)

@app.route("/")
def index():
    return redirect("/apidocs")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

