# Title: Check If Number Is Prime (sqrt Optimization)
# Difficulty: Easy
#
# Description:
# Return True if number is prime, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(4) -> False.
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
        ((2,), True),
        ((4,), False),
        ((17,), True),
        ((1,), False),
        ((97,), True),
        ((100,), False),
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
