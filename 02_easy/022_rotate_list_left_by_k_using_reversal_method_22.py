# Title: Rotate List Left By K Using Reversal Method
# Difficulty: Easy
#
# Description:
# Rotate list left by k using reversal method and return the result.
#

def solve(lst, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3, 4], 1), [2, 3, 4, 1]),
        (([1], 3), [1]),
        (([], 1), []),
        (([1, 2], 2), [1, 2]),
        (([1, 2, 3], 2), [3, 1, 2]),
        (([0, 0, 1], 1), [0, 1, 0]),
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
