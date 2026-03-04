# Title: Check Whether Number Is Abundant, Deficient, Or Perfect
# Difficulty: Easy
#
# Description:
# Given an integer n, classify it as "abundant", "deficient", or "perfect" based on the sum of its proper divisors.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(12) -> 'abundant'.
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
        ((6,), 'perfect'),
        ((12,), 'abundant'),
        ((8,), 'deficient'),
        ((1,), 'deficient'),
        ((28,), 'perfect'),
        ((18,), 'abundant'),
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
