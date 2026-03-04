# Title: Calculate Percentage From Marks
# Difficulty: Very Easy
#
# Description:
# Calculate percentage from marks and return the result.
#
# Example: solve(450, 500) -> 90.0.
# Example: solve(0, 500) -> 0.0.
#
# Tags: [integer]
#

def solve(n1, n2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((450, 500), 90.0),
        ((0, 500), 0.0),
        ((250, 500), 50.0),
        ((500, 500), 100.0),
        ((125, 250), 50.0),
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
