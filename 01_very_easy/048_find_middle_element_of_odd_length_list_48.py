# Title: Find Middle Element Of Odd-length List
# Difficulty: Very Easy
#
# Description:
# Return middle element of odd-length list.
#
# Example: solve([1, 2, 3]) -> 2.
# Example: solve([5]) -> 5.
#
# Tags: [list] [array]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3],), 2),
        (([5],), 5),
        (([1, 3, 5, 7, 9],), 5),
        (([-3, -2, -1],), -2),
        (([0, 1, 2],), 1),
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
