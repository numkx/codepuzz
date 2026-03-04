# Title: Find List Length
# Difficulty: Very Easy
#
# Description:
# Given array/list input, return list length.
#
# Example: solve([1, 2, 3]) -> 3.
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
        (([1, 2, 3],), 3),
        (([],), 0),
        (([5],), 1),
        ((['a', 'b'],), 2),
        (([None, None, None],), 3),
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
