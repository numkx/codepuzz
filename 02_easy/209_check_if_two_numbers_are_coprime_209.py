# Title: Check If Two Numbers Are Coprime
# Difficulty: Easy
#
# Description:
# Given two integers, return True if their greatest common divisor is 1, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(12, 18) -> False.
# Example: solve(0) -> 0.
#
# Tags: [integer] [math]
#

def solve(a, b):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((8, 15), True),
        ((12, 18), False),
        ((17, 4), True),
        ((21, 14), False),
        ((35, 64), True),
        ((13, 27), True),
        ((0, 0), False),
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
