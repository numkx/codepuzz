# Title: Find Largest Adjacent Difference
# Difficulty: Very Easy
#
# Description:
# Return largest adjacent difference.
#
# Example: solve([1, 4, 2]) -> 3.
# Example: solve([5]) -> 0.
#
# Tags: [list] [array]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 4, 2],), 3),
        (([5],), 0),
        (([1, 1],), 0),
        (([-1, 2, -3],), 5),
        (([2, 9, 4],), 7),
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
