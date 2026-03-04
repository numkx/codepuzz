# Title: Course Schedule Ii
# Difficulty: Medium
#
# Description:
# Return one valid order to finish all courses, or an empty list if impossible.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve((3, [[0, 1], [1, 2]])) -> True.
# Example: solve((3, [[0, 1]])) -> False.
#
# Tags: [graph]
#

def solve(t):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (((3, [[0, 1], [1, 2]]),), True),
        (((3, [[0, 1]]),), False),
        (((1, []),), True),
        (((4, [[0, 1], [2, 3]]),), False),
        (((4, [[0, 1], [1, 2], [2, 3]]),), True),
        (((2, []),), False),
        (((),), False),
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
