# Title: Check If Number Is Power Of Ten
# Difficulty: Easy
#
# Description:
# Given an integer n, return True if n is a power of ten, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(10) -> True.
# Example: solve(0) -> 0.
#
# Tags: [integer] [math]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1,), True),
        ((10,), True),
        ((1000,), True),
        ((500,), False),
        ((0,), False),
        ((100000,), True),
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
