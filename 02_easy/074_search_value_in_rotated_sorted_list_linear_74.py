# Title: Search Value In Rotated Sorted List (linear)
# Difficulty: Easy
#
# Description:
# Return the result after applying the required operation to the input.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([3, 1, 2],), [1, 2, 3]),
        (([],), []),
        (([1],), [1]),
        (([2, 2, 1],), [1, 2, 2]),
        (([-1, 3, 0],), [-1, 0, 3]),
        (([5, 4],), [4, 5]),
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
