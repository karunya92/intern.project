import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from config.db_config import DATABASE_PATH


def ensure_database_dir() -> None:
    Path(DATABASE_PATH).parent.mkdir(parents=True, exist_ok=True)


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    ensure_database_dir()
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()
