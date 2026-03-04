# Title: Get Common Elements Of Two Lists
# Difficulty: Very Easy
#
# Description:
# Return get common elements of two lists.
#
# Example: solve([1, 2, 3], [2, 3, 4]) -> [2, 3].
# Example: solve([], [1]) -> [].
#

def solve(lst1, lst2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3], [2, 3, 4]), [2, 3]),
        (([], [1]), []),
        (([1], []), []),
        (([1, 1], [1, 2]), [1]),
        ((['a', 'b'], ['b', 'c']), ['b']),
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
