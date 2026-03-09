#!/usr/bin/env python3
"""Nepes Colorscheme Showcase — Python syntax highlighting demo."""

from dataclasses import dataclass, field
from typing import Optional
import asyncio
import math

# Constants
MAX_RETRIES = 3
PI = 3.14159265
ENABLED = True
NOTHING = None

@dataclass
class SensorReading:
    """A single measurement from an equipment sensor."""
    equipment_id: str
    value: float
    unit: str = "nm"
    timestamp: Optional[str] = None
    tags: list[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return 0.0 <= self.value <= 9999.99

    def to_dict(self) -> dict:
        return {
            "id": self.equipment_id,
            "value": round(self.value, 2),
            "unit": self.unit,
            "valid": self.is_valid,
        }


async def process_readings(readings: list[SensorReading]) -> dict[str, float]:
    """Process sensor readings and return statistics."""
    if not readings:
        raise ValueError("Empty readings list")

    valid = [r for r in readings if r.is_valid]
    invalid_count = len(readings) - len(valid)

    if invalid_count > 0:
        print(f"WARNING: {invalid_count} invalid readings skipped")

    values = [r.value for r in valid]
    mean = sum(values) / len(values)
    std_dev = math.sqrt(sum((v - mean) ** 2 for v in values) / len(values))

    # Statistical thresholds
    result = {
        "count": len(valid),
        "mean": round(mean, 4),
        "std_dev": round(std_dev, 4),
        "min": min(values),
        "max": max(values),
        "range": max(values) - min(values),
    }

    await asyncio.sleep(0.01)  # simulate async I/O
    return result


def main():
    readings = [
        SensorReading("EQP-001", 42.5, "nm", tags=["chamber-a"]),
        SensorReading("EQP-002", 99.1, "μm"),
        SensorReading("EQP-003", -1.0, "nm"),  # invalid
        SensorReading("EQP-004", 55.8, "nm", tags=["chamber-b", "urgent"]),
    ]

    for i, r in enumerate(readings, start=1):
        status = "OK" if r.is_valid else "ERR"
        print(f"  [{status}] #{i}: {r.equipment_id} = {r.value}{r.unit}")

    try:
        stats = asyncio.run(process_readings(readings))
        print(f"\nResults: {stats}")
    except ValueError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
