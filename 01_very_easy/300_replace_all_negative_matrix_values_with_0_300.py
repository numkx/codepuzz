# Title: Replace All Negative Matrix Values With 0
# Difficulty: Very Easy
#
# Description:
# Replace all negative matrix values with 0 and return the updated result.
#
# Example: solve([[1, -2], [-3, 4]]) -> [[1, 0], [0, 4]].
# Example: solve([[1]]) -> [[1]].
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([[1, -2], [-3, 4]],), [[1, 0], [0, 4]]),
        (([[1]],), [[1]]),
        (([[-1]],), [[0]]),
        (([[]],), [[]]),
        (([[0, -1]],), [[0, 0]]),
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
