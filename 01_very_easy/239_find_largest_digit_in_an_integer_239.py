# Title: Find Largest Digit In An Integer
# Difficulty: Very Easy
#
# Description:
# Return largest digit in an integer.
#
# Example: solve(123) -> 3.
# Example: solve(0) -> 0.
#
# Tags: [integer]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((123,), 3),
        ((0,), 0),
        ((907,), 9),
        ((-321,), 3),
        ((555,), 5),
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
