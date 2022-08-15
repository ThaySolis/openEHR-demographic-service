import os

PLAIN_HTTP = (os.environ.get("PLAIN_HTTP", "no").lower() == "yes")
SERVER_PORT = int(os.environ.get("SERVER_PORT", "12002"))
SYSTEM_ID = os.environ.get("SYSTEM_ID", "demographic.system")
INCLUDE_USAGE_STATISTICS = (os.environ.get("INCLUDE_USAGE_STATISTICS", "no").lower() == "yes")
USAGE_STATISTICS_MAX_SAMPLES = int(os.environ.get("USAGE_STATISTICS_MAX_SAMPLES", "1000"))

AUTH_USERNAME = os.environ.get("AUTH_USERNAME", "demographic_user")
AUTH_PASSWORD = os.environ.get("AUTH_PASSWORD", "demographic_password")

DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PORT = int(os.environ.get("DB_PORT", "27018"))
DB_USERNAME = os.environ.get("DB_USERNAME", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "example")
