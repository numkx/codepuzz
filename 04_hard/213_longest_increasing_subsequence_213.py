# Title: Longest Increasing Subsequence
# Difficulty: Hard
#
# Description:
# Return the length of the longest strictly increasing subsequence (keep order; items do not need to be adjacent).
#
# Example: solve([10, 9, 2, 5, 3, 7, 101, 18]) -> 4.
# Example: solve([0, 1, 0, 3, 2, 3]) -> 4.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([10, 9, 2, 5, 3, 7, 101, 18],), 4),
        (([0, 1, 0, 3, 2, 3],), 4),
        (([7, 7, 7, 7],), 1),
        (([],), 0),
        (([1],), 1),
        (([4, 10, 4, 3, 8, 9],), 3),
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
