# Title: Split List Into K Chunks As Evenly As Possible
# Difficulty: Easy
#
# Description:
# Return split list into k chunks as evenly as possible.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([0, 1, 0, 2]) -> [1, 2, 0, 0].
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
        (([0, 1, 0, 2],), [1, 2, 0, 0]),
        (([],), []),
        (([1],), [1]),
        (([1, 2, 3],), [1, 2, 3]),
        (([0, 0],), [0, 0]),
        (([-1, 1],), [1, -1]),
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
