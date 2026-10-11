"""Generated fictional observations, deterministic descriptive analysis only."""

import csv
import json
from decimal import Decimal
from pathlib import Path


def describe(path: Path) -> dict[str, int | str]:
    with path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    if len(rows) != 12 or any(set(row) != {"record_id", "value"} for row in rows):
        raise ValueError("Exactly twelve controlled synthetic records required")
    ids = [int(row["record_id"]) for row in rows]
    if len(set(ids)) != 12 or set(ids) != set(range(1, 13)):
        raise ValueError("Unique complete fixture identities required")
    values = [Decimal(row["value"]) for row in rows]
    if not all(value.is_finite() for value in values):
        raise ValueError("Finite synthetic values required")
    return {
        "records": len(rows),
        "mean": str(sum(values) / len(values)),
        "minimum": str(min(values)),
        "maximum": str(max(values)),
    }


if __name__ == "__main__":
    print(
        json.dumps(
            describe(Path(__file__).parent / "data/sensor.csv"),
            sort_keys=True,
            separators=(",", ":"),
        )
    )
