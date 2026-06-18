from modules.report_module import calculate_completion


def test_calculate_completion():
    tasks = [{"status": "Completed"}, {"status": "In Progress"}]
    assert calculate_completion(tasks) == 50
