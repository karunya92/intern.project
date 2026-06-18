from pathlib import Path

import pandas as pd

from config.config import REPORT_EXPORT_DIR


def export_csv(records: list[dict], filename: str) -> Path:
    REPORT_EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    target = REPORT_EXPORT_DIR / filename
    pd.DataFrame(records).to_csv(target, index=False)
    return target
