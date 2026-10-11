"""Checks the controlled program; not predictive or statistical validation."""

import tempfile
import unittest
from pathlib import Path

from analysis import describe


class AnalysisTests(unittest.TestCase):
    def test_known_descriptive_output(self):
        self.assertEqual(
            describe(Path(__file__).parent / "data/sensor.csv"),
            {"records": 12, "mean": "21", "minimum": "10", "maximum": "32"},
        )

    def test_duplicate_record_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.csv"
            path.write_text("record_id,value\n" + "1,10\n" * 12)
            with self.assertRaises(ValueError):
                describe(path)

    def test_missing_observation_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.csv"
            path.write_text("record_id,value\n1,10\n")
            with self.assertRaises(ValueError):
                describe(path)


if __name__ == "__main__":
    unittest.main()
