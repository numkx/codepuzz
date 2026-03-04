# Title: Multiply Each List Element By 2
# Difficulty: Very Easy
#
# Description:
# Multiply each list element by 2 and return the result.
#
# Example: solve([1, 2, 3]) -> [2, 4, 6].
# Example: solve([]) -> [].
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), [2, 4, 6]),
        (([],), []),
        (([-1, 0],), [-2, 0]),
        (([5],), [10]),
        (([2, 2],), [4, 4]),
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
