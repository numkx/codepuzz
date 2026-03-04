# Title: Check If Number Is Even
# Difficulty: Very Easy
#
# Description:
# Return True if number is even, otherwise return False.
#
# Example: solve(2) -> True.
# Example: solve(3) -> False.
#
# Tags: [integer]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((2,), True),
        ((3,), False),
        ((0,), True),
        ((-4,), True),
        ((-5,), False),
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
