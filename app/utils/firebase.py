import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Load environment variables from .env file
load_dotenv()

# Get the path to the Firebase service account credentials
firebase_cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "app/secrets/firebase-credentials.json")

# Validate that the credentials file exists
if not os.path.exists(firebase_cred_path):
    raise FileNotFoundError(f"Firebase credentials not found at: {firebase_cred_path}")

# Initialize Firebase app if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_cred_path)
    firebase_admin.initialize_app(cred)

# Firestore client instance
db = firestore.client()
