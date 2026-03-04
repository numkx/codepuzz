# Title: Count Digits In An Integer
# Difficulty: Very Easy
#
# Description:
# Return the count of digits in an integer.
#
# Example: solve(0) -> 1.
# Example: solve(7) -> 1.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((0,), 1),
        ((7,), 1),
        ((123,), 3),
        ((-456,), 3),
        ((1000,), 4),
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
