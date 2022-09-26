import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "13146123").strip()
API_HASH = os.getenv("API_HASH", "53e10a257baaddea9c413a0c4249e731").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5663138972:AAHF9IbIfmzZUTxQuWtinZ3KaymRM1dYo0w").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://wrboowft:4GkTRolIXOj4vSQVUtFB2ZYgSAluhAAT@heffalump.db.elephantsql.com/wrboowft").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "RomeoBot_OP")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
