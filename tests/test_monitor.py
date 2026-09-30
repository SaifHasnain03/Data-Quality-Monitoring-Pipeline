from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.monitor import run

def test_report_contains_checks():
    report = run()
    assert "checks" in report
    assert report["total_checks"] == 4

def test_injected_issues_are_detected():
    report = run()
    assert report["status"] == "REVIEW"
    assert report["negative_income"] > 0
    assert report["duplicate_record_ids"] > 0
