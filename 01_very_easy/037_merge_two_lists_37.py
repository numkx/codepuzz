# Title: Merge Two Lists
# Difficulty: Very Easy
#
# Description:
# Merge two lists and return the result.
#
# Example: solve([1, 2], [3, 4]) -> [1, 2, 3, 4].
# Example: solve([], [1]) -> [1].
#
# Tags: [list] [array]
#

def solve(lst1, lst2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2], [3, 4]), [1, 2, 3, 4]),
        (([], [1]), [1]),
        (([1], []), [1]),
        (([], []), []),
        ((['a'], ['b']), ['a', 'b']),
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
