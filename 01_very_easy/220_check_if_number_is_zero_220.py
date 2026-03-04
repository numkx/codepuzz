# Title: Check If Number Is Zero
# Difficulty: Very Easy
#
# Description:
# Return True if number is zero, otherwise return False.
#
# Example: solve(0) -> True.
# Example: solve(1) -> False.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((0,), True),
        ((1,), False),
        ((-1,), False),
        ((99,), False),
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
