# Title: Count Elements Greater Than X
# Difficulty: Very Easy
#
# Description:
# Return the count of elements greater than x.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([1, 2, 3], 2) -> 1.
# Example: solve([], 1) -> 0.
#
# Tags: [list] [array] [integer]
#

def solve(lst, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3], 2), 1),
        (([], 1), 0),
        (([5, 5], 4), 2),
        (([-1, 0], 0), 0),
        (([1, 1, 1], 1), 0),
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
