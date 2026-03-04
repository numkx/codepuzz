# Title: Find Second Smallest Element
# Difficulty: Very Easy
#
# Description:
# Return second smallest element.
#
# Example: solve([1, 2, 3]) -> 2.
# Example: solve([5, 5, 4]) -> 5.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), 2),
        (([5, 5, 4],), 5),
        (([9, 1],), 9),
        (([-1, -2, -3],), -2),
        (([1, 1, 1, 2],), 1),
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
