# Title: Path Sum Variant
# Difficulty: Hard
#
# Description:
# Given an array/list and any required parameters, compute the required path-based result.
# Return the computed result.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), 2),
        (([],), 0),
        (([1],), 1),
        (([1, None, 2],), 2),
        (([3, 9, 20, None, None, 15, 7],), 3),
        (([1, 2, None, 3],), 3),
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
