from dotenv import load_dotenv
import os

load_dotenv()

class GoogleConfig:
    b64_creds = os.environ.get("GOOGLE_SERVICE_CREDENTIALS")

class Postgresql:
    conn_string = os.environ.get("DATABASE_URL")

