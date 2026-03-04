# Title: Merge Two Sorted Lists
# Difficulty: Medium
#
# Description:
# Merge two sorted lists and return the result.
#
# Example: solve([1, 2, 4], [1, 3, 4]) -> [1, 1, 2, 3, 4, 4].
# Example: solve([], []) -> [].
#

def solve(lst1, lst2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        (([], []), []),
        (([], [0]), [0]),
        (([1], []), [1]),
        (([1, 3, 5], [2, 4]), [1, 2, 3, 4, 5]),
        (([1, 1], [1]), [1, 1, 1]),
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
