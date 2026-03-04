# Title: Remove Duplicates From An Unsorted List While Preserving Order
# Difficulty: Easy
#
# Description:
# Remove duplicates from an unsorted list while preserving order and return the result.
#
# Example: solve([1, 2, 2, 3]) -> [1, 2, 3].
# Example: solve([]) -> [].
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 2, 3],), [1, 2, 3]),
        (([],), []),
        (([1],), [1]),
        (([5, 5, 5],), [5]),
        (([3, 1, 2, 1],), [3, 1, 2]),
        (([0, 0, 1],), [0, 1]),
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
