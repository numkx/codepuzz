# Title: Check If Year Is Leap Year
# Difficulty: Very Easy
#
# Description:
# Return True if year is leap year, otherwise return False.
#
# Example: solve(2000) -> True.
# Example: solve(1900) -> False.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((2000,), True),
        ((1900,), False),
        ((2024,), True),
        ((2023,), False),
        ((2400,), True),
    ]
    passed = 0
    for args, expected in tests:
        if not isinstance(args, tuple):
            args = (args,)
        try:
            result = solve(*args)
            ok = result == expected
        except Exception as e:
            result = f"<error: {type(e).__name__}>"
            ok = False
        status = "passed" if ok else "failed"
        print(f"solve{args} == {expected} -> {result} ({status})")
        if ok:
            passed += 1
    print(f"{passed}/{len(tests)} tests passed")
