# app/utils/firebase.py

import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()

firebase_cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "app/secrets/firebase-credentials.json")

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_cred_path)
    firebase_admin.initialize_app(cred)

# 👇 This is the missing line causing ImportError
db = firestore.client()
