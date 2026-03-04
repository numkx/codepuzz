# Title: Check If It Is A Straight Line
# Difficulty: Medium
#
# Description:
# Return True if it is a straight line, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([[1, 1], [2, 2], [3, 4], [4, 5]]) -> False.
# Example: solve(0) -> 0.
#
# Tags: [geometry] [math]
#

def solve(points):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],), True),
        (([[1, 1], [2, 2], [3, 4], [4, 5]],), False),
        (([[0, 0], [0, 1], [0, 2]],), True),
        (([[1, 2], [2, 2], [3, 2]],), True),
        (([[1, 1], [2, 3], [3, 5]],), True),
        (([[1, 1], [2, 2], [3, 3], [3, 4]],), False),
        (([[]],), False),
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
