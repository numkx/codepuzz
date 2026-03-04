# Title: Square Each List Element
# Difficulty: Very Easy
#
# Description:
# Return square each list element.
#
# Example: solve([1, 2, 3]) -> [1, 4, 9].
# Example: solve([]) -> [].
#
# Tags: [list] [array]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), [1, 4, 9]),
        (([],), []),
        (([-1, 0],), [1, 0]),
        (([5],), [25]),
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
