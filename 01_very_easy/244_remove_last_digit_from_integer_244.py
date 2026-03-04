# Title: Remove Last Digit From Integer
# Difficulty: Very Easy
#
# Description:
# Remove last digit from integer and return the updated result.
#
# Example: solve(123) -> 12.
# Example: solve(5) -> 0.
#
# Tags: [integer]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((123,), 12),
        ((5,), 0),
        ((0,), 0),
        ((-123,), -12),
        ((10,), 1),
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
