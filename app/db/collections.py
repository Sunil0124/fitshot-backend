from google.cloud.firestore_v1 import CollectionReference
from app.utils.firebase import db

# Firestore collection references
users_collection: CollectionReference = db.collection("users")
trainers_collection: CollectionReference = db.collection("trainers")
appointments_collection: CollectionReference = db.collection("appointments")
orgs_collection: CollectionReference = db.collection("organizations")
domains_collection: CollectionReference = db.collection("domains")
themes_collection: CollectionReference = db.collection("themes")
