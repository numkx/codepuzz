# Title: Number Of Subarrays Of Size K And Average Greater Than Threshold
# Difficulty: Hard
#
# Description:
# Return the number of subarrays of size k and average greater than threshold.
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
