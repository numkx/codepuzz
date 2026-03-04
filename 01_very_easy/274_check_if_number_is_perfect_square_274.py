# Title: Check If Number Is Perfect Square
# Difficulty: Very Easy
#
# Description:
# Return True if number is perfect square, otherwise return False.
#
# Example: solve(1) -> True.
# Example: solve(4) -> True.
#
# Tags: [integer]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1,), True),
        ((4,), True),
        ((5,), False),
        ((0,), True),
        ((49,), True),
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
