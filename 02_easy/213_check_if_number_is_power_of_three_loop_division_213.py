# Title: Check If Number Is Power Of Three (loop Division)
# Difficulty: Easy
#
# Description:
# Return True if number is power of three, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(27) -> True.
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
        ((27,), True),
        ((45,), False),
        ((0,), False),
        ((243,), True),
        ((10,), False),
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
