# Title: Insert Delete GetRandom O1 Duplicates Allowed
# Difficulty: Hard
#
# Description:
# Given the provided input, support insert, delete, and random retrieval in average O(1) time.
# Return the computed result.
#

def solve(lst, n1, n2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3], 1, 9), [1, 9, 2, 3]),
        (([], 0, 5), [5]),
        (([1], 1, 2), [1, 2]),
        (([1, 2], 0, 0), [0, 1, 2]),
        (([1, 2], 2, 3), [1, 2, 3]),
        (([1, 1], 1, 1), [1, 1, 1]),
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
