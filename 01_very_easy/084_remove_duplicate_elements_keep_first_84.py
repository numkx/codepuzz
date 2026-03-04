# Title: Remove Duplicate Elements (keep First)
# Difficulty: Very Easy
#
# Description:
# Remove duplicate elements and return the updated result.
#
# Example: solve([1, 2, 2, 3, 1]) -> [1, 2, 3].
# Example: solve([]) -> [].
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 2, 3, 1],), [1, 2, 3]),
        (([],), []),
        (([1, 1, 1],), [1]),
        ((['a', 'b', 'a'],), ['a', 'b']),
        (([2, 3],), [2, 3]),
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
