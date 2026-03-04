# Title: Search Insert Position
# Difficulty: Medium
#
# Description:
# Solve search insert position and return the result.
#
# Example: solve([1, 3, 5, 6], 5) -> 2.
# Example: solve([1, 3, 5, 6], 2) -> 1.
#

def solve(lst, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 3, 5, 6], 5), 2),
        (([1, 3, 5, 6], 2), 1),
        (([1, 3, 5, 6], 7), 4),
        (([1, 3, 5, 6], 0), 0),
        (([], 5), 0),
        (([1], 0), 0),
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
