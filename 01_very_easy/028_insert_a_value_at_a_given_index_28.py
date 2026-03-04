# Title: Insert A Value At A Given Index
# Difficulty: Very Easy
#
# Description:
# Insert a value at a given index and return the updated result.
#
# Example: solve([1, 2, 3], 1, 9) -> [1, 9, 2, 3].
# Example: solve([], 0, 5) -> [5].
#

def solve(lst, n, x):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3], 1, 9), [1, 9, 2, 3]),
        (([], 0, 5), [5]),
        (([9], 1, 8), [9, 8]),
        ((['a', 'c'], 1, 'b'), ['a', 'b', 'c']),
        (([1, 1], 2, 1), [1, 1, 1]),
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
