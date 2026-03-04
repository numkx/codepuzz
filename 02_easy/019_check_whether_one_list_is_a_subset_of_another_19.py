# Title: Check Whether One List Is A Subset Of Another
# Difficulty: Easy
#
# Description:
# Return True if one list is a subset of another, otherwise return False.
#
# Example: solve([1, 2, 3]) -> True.
# Example: solve([]) -> True.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), True),
        (([],), True),
        (([1],), True),
        (([1, 1],), True),
        (([2, 1],), False),
        (([0],), True),
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
