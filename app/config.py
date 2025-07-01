import os
from dotenv import load_dotenv

load_dotenv()

FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH", "path/to/your/firebase/credentials.json")
PROJECT_NAME = os.getenv("PROJECT_NAME", "Fitshot")
API_PREFIX = "/api"