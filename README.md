# 🏋️‍♂️ Fitshot Backend

**Fitshot** is a modern fitness tracking platform designed to seamlessly connect **athletes**, **trainers**, and **admins** through a unified digital experience.  
This backend is built using **FastAPI**, providing a **scalable**, **secure**, and **modular** API that powers both the **mobile** and **web** applications.

---

## 📐 UML & ERD Diagrams

### 🔗 UML Diagrams (Figma)

- [📌 UML Diagram (Design File)](https://www.figma.com/design/o7grXz346zl7sIsAj0mFOh/Fitshot-UML-Diagrams?m=auto&t=T1rg7vqrFOAVz9ez-1)  
- [🧩 UML Diagram (Board View)](https://www.figma.com/board/Qynqkyf4CcqQ5HAOwKcexQ/UML-Diagram?node-id=0-1&p=f&t=wlaZjXYzl3bSWSPp-0)

### 🗂️ ERD Diagram (Database Schema)

- [🔍 Fitshot ERD - DrawSQL](https://drawsql.app/teams/fitshot/diagrams/fitshot-erd-diagram)

---

## 🚀 Features

- 🧑‍🤝‍🧑 User Roles: Athlete, Trainer, Admin
- 📆 Appointment Booking between Athletes and Trainers
- 📝 Session Notes and Trainer Availability
- 🔐 Firebase JWT-based Authentication & Role Authorization
- 🔔 Notifications & Health Data Integration (planned)
- 📊 RESTful API for both Mobile and Web Clients

---

## 🛠️ Tech Stack

- **Framework**: FastAPI (Python)
- **Database**: Firestore (via Firebase Admin SDK)
- **Auth**: Firebase JWT Authentication
- **Hosting**: Google Cloud Platform (GCP)
- **Docs**: OpenAPI/Swagger (`/docs`)
- **Containerization**: Docker (Planned)
- **CI/CD**: GitHub Actions (Planned)

---

## 📦 Project Structure

```bash
fitshot-backend/
├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── config.py            # Configuration and env loading
│   ├── routes/              # API route definitions
│   ├── schemas/             # Pydantic models for request/response
│   ├── services/            # Business logic and Firestore queries
│   ├── models/              # Enum and type models
│   ├── utils/               # Auth, Firebase init, helper functions
│   └── db/collections.py    # Firestore collection references
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 📬 API Docs

- Visit: [`http://localhost:8000/docs`](http://localhost:8000/docs)
- Interactive Swagger UI for testing all endpoints

---

## 📄 License

MIT © 2025 Fitshot Team
