from services.analytics_service import attendance_percentage


def test_attendance_percentage():
    records = [{"status": "Present"}, {"status": "Absent"}]
    assert attendance_percentage(records) == 50
