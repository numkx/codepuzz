# Title: Print Numbers From 1 To N
# Difficulty: Very Easy
#
# Description:
# Return numbers from 1 to n.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(1) -> [1].
# Example: solve(3) -> [1, 2, 3].
#
# Tags: [integer]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1,), [1]),
        ((3,), [1, 2, 3]),
        ((0,), []),
        ((5,), [1, 2, 3, 4, 5]),
        ((2,), [1, 2]),
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
