# Title: Search A 2D Matrix
# Difficulty: Hard
#
# Description:
# Given a 2D matrix and target, return True if target exists in the matrix, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) -> False.
# Example: solve([[0]]) -> [[0]].
#
# Tags: [matrix] [binary search]
#

def solve(lst, target):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True),
        (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False),
        (([], 1), False),
        (([[1]], 1), True),
        (([[1]], 2), False),
        (([[1, 2], [3, 4]], 4), True),
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
