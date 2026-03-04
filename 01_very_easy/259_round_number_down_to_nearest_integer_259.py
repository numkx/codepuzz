# Title: Round Number Down To Nearest Integer
# Difficulty: Very Easy
#
# Description:
# Return round number down to nearest integer.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(2.9) -> 2.
# Example: solve(2.0) -> 2.
#
# Tags: [number]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((2.9,), 2),
        ((2.0,), 2),
        ((-2.1,), -3),
        ((0.0,), 0),
        ((-0.1,), -1),
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
