# Title: Compare Two Lists For Equality
# Difficulty: Very Easy
#
# Description:
# Compare two lists for equality and return the result.
#
# Example: solve([1, 2], [1, 2]) -> True.
# Example: solve([1, 2], [2, 1]) -> False.
#

def solve(lst1, lst2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2], [1, 2]), True),
        (([1, 2], [2, 1]), False),
        (([], []), True),
        (([1], [1, 1]), False),
        ((['a'], ['a']), True),
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
