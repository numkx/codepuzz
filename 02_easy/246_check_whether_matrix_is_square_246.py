# Title: Check Whether Matrix Is Square
# Difficulty: Easy
#
# Description:
# Return True if matrix is square, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([[1, 2, 3], [4, 5, 6]]) -> False.
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
        (([[1, 2], [3, 4]],), True),
        (([[1, 2, 3], [4, 5, 6]],), False),
        (([[1]],), True),
        (([],), False),
        (([[1, 2], [3, 4], [5, 6]],), False),
        (([[0, 0, 0], [0, 0, 0], [0, 0, 0]],), True),
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
