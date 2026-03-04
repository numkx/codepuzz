# Title: Insert A Value At The Beginning Of A List
# Difficulty: Very Easy
#
# Description:
# Insert a value at the beginning of a list and return the updated result.
#
# Example: solve([1, 2, 3], 0) -> [0, 1, 2, 3].
# Example: solve([], 5) -> [5].
#

def solve(lst, x):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3], 0), [0, 1, 2, 3]),
        (([], 5), [5]),
        (([9], 8), [8, 9]),
        ((['b'], 'a'), ['a', 'b']),
        (([1, 1], 1), [1, 1, 1]),
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
