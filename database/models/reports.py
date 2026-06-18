from dataclasses import dataclass


@dataclass
class ReportSummary:
    total_employees: int = 0
    attendance_percentage: int = 0
    completed_tasks: int = 0
