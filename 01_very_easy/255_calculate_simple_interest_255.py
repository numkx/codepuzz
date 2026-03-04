# Title: Calculate Simple Interest
# Difficulty: Very Easy
#
# Description:
# Calculate simple interest and return the result.
#

def solve(n1, n2, n3):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1000, 5, 2), 100.0),
        ((500, 10, 1), 50.0),
        ((100, 0, 5), 0.0),
        ((2000, 3, 3), 180.0),
        ((100, 5, 0), 0.0),
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
