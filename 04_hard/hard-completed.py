#!/usr/bin/env python3
from pathlib import Path
import subprocess
import re

HERE = Path(__file__).resolve().parent
SELF = Path(__file__).name

files = sorted([p for p in HERE.glob("*.py") if p.name != SELF])

incomplete = []
complete = []
passed = []
failed = []

summary_re = re.compile(r"^(\d+)\/(\d+) tests passed$")

for f in files:
    text = f.read_text(encoding="utf-8")
    if "raise NotImplementedError" in text:
        incomplete.append(f.name)
    else:
        complete.append(f.name)

for f in files:
    result = subprocess.run(["python3", str(f)], capture_output=True, text=True)
    out = (result.stdout or "").strip().splitlines()
    summary = next((line for line in reversed(out) if "tests passed" in line), "")
    m = summary_re.match(summary.strip())
    ok = bool(m and m.group(1) == m.group(2) and result.returncode == 0)
    if ok:
        passed.append(f.name)
        print(f"{f.name} -> passed")
    else:
        failed.append(f.name)

print("")
print(f"Completed: {len(complete)}")
print(f"Incomplete: {len(incomplete)}")
print(f"Passed: {len(passed)}")
print(f"Failed: {len(failed)}")
