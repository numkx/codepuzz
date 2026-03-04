# Title: Calculate Cube Of A Number
# Difficulty: Very Easy
#
# Description:
# Calculate cube of a number and return the result.
#
# Example: solve(3) -> 27.
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
        ((3,), 27),
        ((0,), 0),
        ((-3,), -27),
        ((5,), 125),
        ((1,), 1),
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
