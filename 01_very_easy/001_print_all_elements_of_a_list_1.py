# Title: Print All Elements Of A List
# Difficulty: Very Easy
#
# Description:
# Return all elements of a list.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([1, 2, 3]) -> [1, 2, 3].
# Example: solve([]) -> [].
#
# Tags: [list] [array]
#

def solve(x):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), [1, 2, 3]),
        (([],), []),
        (((-1, 0, 1),), [-1, 0, 1]),
        (([5],), [5]),
        (([2, 2],), [2, 2]),
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
