def calculate_completion(tasks: list[dict]) -> int:
    if not tasks:
        return 0
    completed = sum(1 for task in tasks if str(task.get("status", "")).lower() == "completed")
    return round((completed / len(tasks)) * 100)
