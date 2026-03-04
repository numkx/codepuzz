# Title: Multiply Two Integers
# Difficulty: Very Easy
#
# Description:
# Multiply two integers and return the result.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(2, 3) -> 6.
# Example: solve(-1, 1) -> -1.
#
# Tags: [integer]
#

def solve(n1, n2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((2, 3), 6),
        ((-1, 1), -1),
        ((0, 8), 0),
        ((7, -2), -14),
        ((-5, -6), 30),
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
