# Title: Remove Adjacent Duplicate Letters Repeatedly Until Stable
# Difficulty: Easy
#
# Description:
# Remove adjacent duplicate letters repeatedly until stable and return the result.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 2, 3],), [1, 2, 3]),
        (([],), []),
        (([1],), [1]),
        (([5, 5, 5],), [5]),
        (([3, 1, 2, 1],), [3, 1, 2]),
        (([0, 0, 1],), [0, 1]),
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
