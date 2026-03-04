# Title: Palindrome Number
# Difficulty: Medium
#
# Description:
# Given a string (or strings) and any required parameters, check whether the condition is satisfied.
# Return True when the condition holds; otherwise return False.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((121,), True),
        ((-121,), False),
        ((10,), False),
        ((0,), True),
        ((12321,), True),
        ((1001,), True),
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
