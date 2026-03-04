# Title: Check If Number Is Positive
# Difficulty: Very Easy
#
# Description:
# Return True if number is positive, otherwise return False.
#
# Example: solve(1) -> True.
# Example: solve(0) -> False.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1,), True),
        ((0,), False),
        ((-1,), False),
        ((99,), True),
        ((-99,), False),
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
