# Title: Find Last Element Of A List
# Difficulty: Very Easy
#
# Description:
# Return last element of a list.
#
# Example: solve([1, 2, 3]) -> 3.
# Example: solve(['a', 'b']) -> 'b'.
#
# Tags: [list] [array]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), 3),
        ((['a', 'b'],), 'b'),
        (([0],), 0),
        (([-5, -4],), -4),
        (([1, None],), None),
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
