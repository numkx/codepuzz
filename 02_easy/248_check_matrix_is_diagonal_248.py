# Title: Check Matrix Is Diagonal
# Difficulty: Easy
#
# Description:
# Given a matrix, return True if all non-diagonal elements are zero, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([[1, 0], [1, 2]]) -> False.
# Example: solve([[0]]) -> [[0]].
#
# Tags: [matrix]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([[1, 0, 0], [0, 2, 0], [0, 0, 3]],), True),
        (([[1, 0], [1, 2]],), False),
        (([[5]],), True),
        (([[0, 0], [0, 0]],), True),
        (([[1, 0, 0], [0, 0, 0], [0, 0, 3]],), True),
        (([[1, 0, 2], [0, 3, 0], [0, 0, 4]],), False),
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
