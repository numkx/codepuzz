# Title: Find Missing Value From 1..n In List Of Size N-1
# Difficulty: Easy
#
# Description:
# Given the provided input, find missing value from 1..n in list of size n-1.
# Return the resulting list/collection.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), 1),
        (([],), -1),
        (([1],), 0),
        (([5, 4, 3],), 5),
        (([-1, 1],), -1),
        (([9, 9],), 9),
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
