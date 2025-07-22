# 🏋️‍♂️ Fitshot Backend

**Fitshot** is an intelligent fitness and coaching platform that empowers **athletes**, **trainers**, and **organizations** to interact seamlessly through a unified digital experience.  
This **FastAPI** backend is modular, secure, and optimized for scale — built to support both **mobile** and **web** clients.

---

## 🧠 Core Highlights

- ✅ Firebase Firestore-backed multi-tenant database
- 🔐 Firebase Authentication & JWT validation
- 🏢 Organization + Theme customization API
- 📆 Trainer scheduling & athlete appointment booking
- ⚙️ Modular FastAPI architecture with Swagger documentation

---

## 📐 UML & ERD Diagrams

### 🔗 UML Diagrams (Figma)

- [📌 UML Design File](https://www.figma.com/design/o7grXz346zl7sIsAj0mFOh/Fitshot-UML-Diagrams?m=auto&t=T1rg7vqrFOAVz9ez-1)  
- [🧩 UML Board View](https://www.figma.com/board/Qynqkyf4CcqQ5HAOwKcexQ/UML-Diagram?node-id=0-1&p=f&t=wlaZjXYzl3bSWSPp-0)

### 🗂️ ERD Diagram (DrawSQL)

- [🔍 Fitshot ERD Schema](https://drawsql.app/teams/fitshot/diagrams/fitshot-erd-diagram)

---

## 🚀 Features

- 🧑‍🤝‍🧑 **User Roles**: Athlete, Trainer, Admin (via Firebase Auth)
- 🏢 **Organization Management**: Create orgs, update themes
- 🎨 **Theme API**: Set custom branding colors per organization
- 📆 **Appointment Booking**: Manage trainer slots & athlete sessions
- 🔒 **Auth Middleware**: Firebase JWT decoding and role-based protection
- 🧾 **Swagger Schema**: Pydantic models with built-in example schemas
- 🔔 Notifications & Health Sync (planned)

---

## 🛠️ Tech Stack

| Layer            | Technology                     |
|------------------|--------------------------------|
| Backend API      | FastAPI (Python)               |
| Database         | Google Firestore (Firebase)    |
| Auth             | Firebase JWT + Role Guards     |
| Deployment       | Google Cloud Platform (GCP)    |
| API Docs         | Swagger UI (`/docs`)           |
| Containerization | Docker (Planned)               |
| CI/CD            | GitHub Actions (Planned)       |

---

## 📦 Project Structure

```bash
fitshot-backend/
├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── config.py            # Environment loader
│   ├── routes/              # API endpoints by domain
│   ├── schemas/             # Pydantic request/response models
│   ├── services/            # Business logic and Firestore operations
│   ├── utils/               # Firebase, auth, password hashing
│   └── db/
│       └── collections.py   # Firestore collection references
├── secrets/
│   └── firebase-credentials.json  # 🔒 Firebase service account
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
└── README.md

## 🔐 Firebase & Security
✅ Auth: Firebase JWT Authentication
✅ Token Usage: Authorization: Bearer <token> required for protected routes
✅ Password Security: SHA-256 hashed passwords (for org-level use)
✅ Token Validation: Via Firebase Admin SDK

## Setup Instructions

## 1. Clone Repository

git clone https://github.com/sunilganta-dev/fitshot-backend.git
cd fitshot-backend

## 2. Install Dependencies

pip install -r requirements.txt

## 3. Add Firebase Credentials

Save your Firebase Admin SDK private key as:

app/secrets/firebase-credentials.json

## 4. Create .env File

FIREBASE_CREDENTIALS_PATH=app/secrets/firebase-credentials.json

## 5. Run the Server

uvicorn app.main:app --reload

## 6. Access API Docs

Open your browser and visit:

http://localhost:8000/docs


## 🪪 License
© 2025 Chaya Development LLC – All rights reserved.
Part of the Fitshot AI Fitness Ecosystem.