# Title: Two Sum
# Difficulty: Medium
#
# Description:
# Solve two sum and return the result.
#
# Example: solve([2, 7, 11, 15], 9) -> [0, 1].
# Example: solve([3, 2, 4], 6) -> [1, 2].
#

def solve(lst, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
        (([1, 2, 3], 7), []),
        (([0, 4, 3, 0], 0), [0, 3]),
        (([-3, 4, 3, 90], 0), [0, 2]),
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
