# Title: Find First Element Of A List
# Difficulty: Very Easy
#
# Description:
# Return first element of a list.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([1, 2, 3]) -> 1.
# Example: solve(['a', 'b']) -> 'a'.
#
# Tags: [list] [array]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), 1),
        ((['a', 'b'],), 'a'),
        (([0],), 0),
        (([-5, -4],), -5),
        (([None, 1],), None),
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
