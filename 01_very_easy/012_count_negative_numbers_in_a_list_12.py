# Title: Count Negative Numbers In A List
# Difficulty: Very Easy
#
# Description:
# Return the count of negative numbers in a list.
#
# Example: solve([-1, 0, 1, 2]) -> 1.
# Example: solve([]) -> 0.
#
# Tags: [list] [array]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([-1, 0, 1, 2],), 1),
        (([],), 0),
        (([1, 2, 3],), 0),
        (([-1, -2],), 2),
        (([0],), 0),
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
