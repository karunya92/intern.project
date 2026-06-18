def attendance_percentage(records: list[dict]) -> int:
    if not records:
        return 0
    present = sum(1 for row in records if str(row.get("status", "")).lower() == "present")
    return round((present / len(records)) * 100)
