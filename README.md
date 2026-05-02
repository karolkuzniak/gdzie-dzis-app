# 📍 Gdzie Dziś? Event App

REST API for an event discovery and publication platform in Poland.

## 🛠️ Stack

- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose
- **API Documentation:** Swagger UI

## 🚀 Running Locally

### Requirements
- Docker Desktop

### Steps
```bash
git clone https://github.com/karolkuzniak/gdzie-dzis-app.git
cd gdzie-dzis-app
docker compose up --build
```

Open: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/events` | Get all events |
| GET | `/events/{id}` | Get event details |
| POST | `/events` | Create new event |
| DELETE | `/events/{id}` | Delete event |

## 🗺️ Roadmap

- [x] REST API (Flask)
- [x] PostgreSQL database
- [x] Docker containerization
- [x] Swagger UI documentation
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] AWS infrastructure (Terraform)
- [ ] Monitoring (CloudWatch)
