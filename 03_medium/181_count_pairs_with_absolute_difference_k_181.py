# Title: Count Pairs With Absolute Difference K
# Difficulty: Medium
#
# Description:
# Given the provided input, count pairs with absolute difference k.
# Return the computed result.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), 3),
        (([],), 0),
        (([1],), 1),
        (([0, 0],), 2),
        (([-1, 1],), 2),
        (([5, 6, 7, 8],), 4),
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
