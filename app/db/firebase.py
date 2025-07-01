import firebase_admin
from firebase_admin import credentials, firestore
import os

# Load credentials from service account key
firebase_cred_path = os.getenv("FIREBASE_CRED_JSON", "firebase_credentials.json")

# Initialize Firebase App only once
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_cred_path)
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()
