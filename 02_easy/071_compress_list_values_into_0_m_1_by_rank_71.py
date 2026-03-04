# Title: Compress List Values Into 0..m-1 By Rank
# Difficulty: Easy
#
# Description:
# Return compress list values into 0..m-1 by rank.
#
# Example: solve([1, 2, 3]) -> [1, 2, 3].
# Example: solve([]) -> [].
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), [1, 2, 3]),
        (([],), []),
        (([0],), [0]),
        (([-1, 1],), [-1, 1]),
        (([2, 2],), [2, 2]),
        (([5, 6],), [5, 6]),
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
