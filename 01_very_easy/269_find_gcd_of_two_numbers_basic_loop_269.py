# Title: Find Gcd Of Two Numbers (basic Loop)
# Difficulty: Very Easy
#
# Description:
# Given a number/integer input, return gcd of two numbers.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(54, 24) -> 6.
# Example: solve(10, 5) -> 5.
#
# Tags: [integer]
#

def solve(n1, n2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((54, 24), 6),
        ((10, 5), 5),
        ((7, 3), 1),
        ((0, 5), 5),
        ((18, 27), 9),
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
