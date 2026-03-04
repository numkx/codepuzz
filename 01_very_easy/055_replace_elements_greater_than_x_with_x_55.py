# Title: Replace Elements Greater Than X With X
# Difficulty: Very Easy
#
# Description:
# Replace elements greater than x with x and return the result.
#
# Example: solve([1, 5, 3], 3) -> [1, 3, 3].
# Example: solve([], 1) -> [].
#

def solve(lst, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 5, 3], 3), [1, 3, 3]),
        (([], 1), []),
        (([5, 5], 4), [4, 4]),
        (([-1, 0], 0), [-1, 0]),
        (([1, 1], 1), [1, 1]),
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
