# Title: Find All Numbers Disappeared In An Array Variant
# Difficulty: Hard
#
# Description:
# Return all numbers disappeared in an array.
#
# Example: solve([1, 2, 3]) -> 1.
# Example: solve([]) -> -1.
#
# Tags: [array] [list]
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
