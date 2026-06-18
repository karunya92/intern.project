from pathlib import Path

from config.config import PROJECT_ROOT


DATABASE_PATH = PROJECT_ROOT / "data" / "team_lms.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
