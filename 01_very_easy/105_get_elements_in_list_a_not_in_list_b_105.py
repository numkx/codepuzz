# Title: Get Elements In List A Not In List B
# Difficulty: Very Easy
#
# Description:
# Return get elements in list a not in list b.
#
# Example: solve([1, 2, 3], [2, 4]) -> [1, 3].
# Example: solve([], [1]) -> [].
#

def solve(lst1, lst2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3], [2, 4]), [1, 3]),
        (([], [1]), []),
        (([1], []), [1]),
        (([1, 1, 2], [1]), [2]),
        ((['a', 'b'], ['b']), ['a']),
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
