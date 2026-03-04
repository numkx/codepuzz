# Title: Check If Matrix Is Symmetric
# Difficulty: Very Easy
#
# Description:
# Return True if matrix is symmetric, otherwise return False.
#
# Example: solve([[1, 2], [2, 1]]) -> True.
# Example: solve([[1, 0], [2, 1]]) -> False.
#
# Tags: [matrix] [list] [array]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([[1, 2], [2, 1]],), True),
        (([[1, 0], [2, 1]],), False),
        (([[1]],), True),
        (([[1, 2, 3], [2, 4, 5], [3, 5, 6]],), True),
        (([[1, 2], [2, 3]],), False),
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
