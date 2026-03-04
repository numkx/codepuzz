# Title: Find Sum Of Last K Elements
# Difficulty: Very Easy
#
# Description:
# Return sum of last k elements.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([1, 2, 3, 4], 2) -> 7.
# Example: solve([1, 2, 3], 0) -> 0.
#
# Tags: [list] [array] [integer]
#

def solve(lst, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3, 4], 2), 7),
        (([1, 2, 3], 0), 0),
        (([5], 1), 5),
        (([], 0), 0),
        (([1, 1, 1], 2), 2),
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
