from pathlib import Path


APP_NAME = "TEAM LMS"
APP_TITLE = "TEAM LMS Portal"
API_BASE_URL = "http://localhost:8080/api"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
UPLOAD_DIR = PROJECT_ROOT / "streamlit_uploads"
EXPORT_DIR = PROJECT_ROOT / "exports"
REPORT_EXPORT_DIR = EXPORT_DIR / "reports"
SESSION_TIMEOUT_MINUTES = 60
